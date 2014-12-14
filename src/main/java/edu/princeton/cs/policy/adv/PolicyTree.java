package edu.princeton.cs.policy.adv;

import java.util.List;

import net.onrc.openvirtex.elements.OVXMap;
import net.onrc.openvirtex.exceptions.NetworkMappingException;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.openflow.protocol.OFFlowMod;
import org.openflow.protocol.action.OFAction;
import org.openflow.protocol.action.OFActionOutput;

import edu.princeton.cs.hsa.PlumbingSwitch;
import edu.princeton.cs.policy.store.PolicyFlowModStore.PolicyFlowModStoreKey;
import edu.princeton.cs.policy.store.PolicyFlowModStore.PolicyFlowModStoreType;

import net.onrc.openvirtex.messages.OVXFlowMod;

public class PolicyTree {
	
    public enum PolicyOperator {
	Parallel,
	Sequential,
	Override,
	Tenant
    }
    
    public static boolean ActionOutputAsPass = true; // set true for firewall app
    private static Logger logger = LogManager.getLogger(PlumbingSwitch.class.getName());
    
    public PolicyOperator operator;
    public PolicyTree leftChild;
    public PolicyTree rightChild;
    public PolicyACL policyACL;
    public PolicyFlowTable flowTable;
    public Integer tenantId; // only meaningful when operator is Invalid
    
    public PolicyTree() {
	this.operator = PolicyOperator.Tenant;
	this.leftChild = null;
	this.rightChild = null;
	this.policyACL = null;
	this.flowTable = null;
	this.tenantId = -1;
    }
	
    public PolicyTree(Character ch) {
	switch(ch){
	case '+':
	    this.operator = PolicyOperator.Parallel;
	    break;
	case '>':
	    this.operator = PolicyOperator.Sequential;
	    break;
	case '/':
	    this.operator = PolicyOperator.Override;
	    break;
	default:
	    this.operator = PolicyOperator.Tenant;
	    break;
	}
	this.leftChild = null;
	this.rightChild = null;
	this.flowTable = null;
	this.tenantId = -1;
    }
    
    public void initializeFlowTable() throws NetworkMappingException {
	
	switch (this.operator) {
	case Parallel:
	case Sequential:
	case Override:
	    this.policyACL = PolicyACL.composeACL(this.leftChild, this.rightChild, this.operator);
	    break;
	case Tenant:
	    this.policyACL = OVXMap.getInstance().getVirtualNetwork(tenantId).getPolicyACL();
	    break;
	default:
	    break;
	}
	
    }
    
    public PolicyUpdateTable update(OVXFlowMod fm, Integer tenantId) {
	
	PolicyUpdateTable updateTable = null;
	
	switch(this.operator) {
	case Parallel:
	case Sequential:
	case Override:
	    updateTable = updateIncremental(fm, tenantId);
	    break;
	case Tenant: // this is leaf, directly add to flow table
	    if (tenantId == this.tenantId) {
		if (this.policyACL.checkACL(fm)) {
		    // TODO: special case: 1+(1+2), process by 1 with two times
		    updateTable = this.flowTable.update(fm);
		} else {
		    logger.info("acl violation controller:{} flowmod:{} acl:{}",
				tenantId, fm, this.policyACL);
		}
	    } else {
		updateTable = new PolicyUpdateTable();
	    }
	    break;
	default:
	    break;
	}
	
	return updateTable;
    }
	
    private PolicyUpdateTable updateIncremental(OVXFlowMod newFm, Integer tenantId) {
		
	// update children
	PolicyUpdateTable leftUpdateTable = this.leftChild.update(newFm, tenantId);
	PolicyUpdateTable rightUpdateTable = this.rightChild.update(newFm, tenantId);
	
	PolicyUpdateTable updateTable = new PolicyUpdateTable();
	if (this.operator == PolicyOperator.Parallel ||
	    this.operator == PolicyOperator.Sequential) {
	    
	    // add
	    /* leftUpdateTable.addFlowMods are flow mods to be recursively added
	       to parent via composition with rightUpdateTable.addFlowMods. */
	    for (OVXFlowMod fm1 : leftUpdateTable.addFlowMods) {
		
		if (this.operator == PolicyOperator.Sequential) {
		    boolean flag = false;
		    if (fm1.getActions().isEmpty()) {
			flag = true;
		    }
		    if (!ActionOutputAsPass) {
			for (OFAction action : fm1.getActions()) {
			    if (action instanceof OFActionOutput) {
				flag = true;
				break;
			    }
			}
		    }
		    if (flag) {
			OVXFlowMod composedFm = null;
			//try {
			    composedFm = fm1.clone();
			    composedFm.setPriority(
				(short) (fm1.getPriority() *
					 PolicyCompositionUtil.SEQUENTIAL_SHIFT));
			    /*} catch (CloneNotSupportedException e) {
			    e.printStackTrace();
			    }*/
			
			composedFm.addChildrenFlowMods(fm1.getChildrenFlowMods());
			this.flowTable.addFlowMod(composedFm);
			leftChild.flowTable.addGeneratedParentFlowMod(fm1, composedFm);
			updateTable.addFlowMods.add(composedFm);
			continue;
		    }
		} // END operator = sequential
		
		List<OVXFlowMod> potentialFlowMods = rightChild.flowTable.getPotentialFlowMods(fm1);
		for (OVXFlowMod fm2: potentialFlowMods) {
		    
		    OVXFlowMod composedFm = null;
		    if (this.operator == PolicyOperator.Parallel) {
			composedFm = PolicyCompositionUtil.parallelComposition(fm1, fm2);
		    } else {
			composedFm = PolicyCompositionUtil.sequentialComposition(fm1, fm2);
		    }
		    
		    if (composedFm != null) {
			composedFm.addChildrenFlowMods(fm1.getChildrenFlowMods());
			composedFm.addChildrenFlowMods(fm2.getChildrenFlowMods());
			this.flowTable.addFlowMod(composedFm);
			leftChild.flowTable.addGeneratedParentFlowMod(fm1, composedFm);
			rightChild.flowTable.addGeneratedParentFlowMod(fm2, composedFm);
			updateTable.addFlowMods.add(composedFm);
		    }
		}
	    }
	    
	    for (OVXFlowMod fm2 : rightUpdateTable.addFlowMods) {
		
		List<OVXFlowMod> leftTableWithoutAdd = PolicyCompositionUtil
		    .diffFlowMods(leftChild.flowTable.getPotentialFlowMods(fm2),
				  leftUpdateTable.addFlowMods);
		for (OVXFlowMod fm1 : leftTableWithoutAdd) {
		    
		    if (this.operator == PolicyOperator.Sequential) {
			boolean flag = false;
			if (fm1.getActions().isEmpty()) {
			    flag = true;
			}
			if (!ActionOutputAsPass) {
			    for (OFAction action : fm1.getActions()) {
				if (action instanceof OFActionOutput) {
				    flag = true;
				    break;
				}
			    }
			}
			if (flag) {
			    continue;
			}
		    }
					
		    OVXFlowMod composedFm = null;
		    if (this.operator == PolicyOperator.Parallel) {
			composedFm = PolicyCompositionUtil.parallelComposition(fm1, fm2);
		    } else {
			composedFm = PolicyCompositionUtil.sequentialComposition(fm1, fm2);
		    }
		    if (composedFm != null) {
			this.flowTable.addFlowMod(composedFm);
			composedFm.addChildrenFlowMods(fm1.getChildrenFlowMods());
			composedFm.addChildrenFlowMods(fm2.getChildrenFlowMods());
			leftChild.flowTable.addGeneratedParentFlowMod(fm1, composedFm);
			rightChild.flowTable.addGeneratedParentFlowMod(fm2, composedFm);
			updateTable.addFlowMods.add(composedFm);
		    }
		}
	    }
	    
	    // delete
	    for (OVXFlowMod fm : leftUpdateTable.deleteFlowMods) {
		List<OVXFlowMod> generatedParentFlowMods =
		    leftChild.flowTable.getGenerateParentFlowMods(fm);
		List<OVXFlowMod> deletedFlowMods =
		    this.flowTable.deleteFlowMods(generatedParentFlowMods);
		updateTable.deleteFlowMods.addAll(deletedFlowMods);
	    }
	    for (OVXFlowMod fm : rightUpdateTable.deleteFlowMods) {
		List<OVXFlowMod> generatedParentFlowMods =
		    rightChild.flowTable.getGenerateParentFlowMods(fm);
		List<OVXFlowMod> deletedFlowMods =
		    this.flowTable.deleteFlowMods(generatedParentFlowMods);
		updateTable.deleteFlowMods.addAll(deletedFlowMods);
	    }
	    leftChild.flowTable.deleteGenerateParentFlowModKeys(leftUpdateTable.deleteFlowMods);
	    rightChild.flowTable.deleteGenerateParentFlowModKeys(rightUpdateTable.deleteFlowMods);
	} // END parallel || sequential

	else if (this.operator == PolicyOperator.Override) {
	    
	    // add
	    for (OVXFlowMod fm : leftUpdateTable.addFlowMods) {
		OVXFlowMod addFm = null;
		//try {
		    addFm = fm.clone();
		    /*} catch (CloneNotSupportedException e) {
		    e.printStackTrace();
		    }*/
		addFm.setPriority((short) (addFm.getPriority() *
					   PolicyCompositionUtil.OVERRIDE_SHIFT));
		this.flowTable.addFlowMod(addFm);
		leftChild.flowTable.addGeneratedParentFlowMod(fm, addFm);
		updateTable.addFlowMods.add(addFm);
	    }
	    
	    for (OVXFlowMod fm : rightUpdateTable.addFlowMods) {
		OVXFlowMod addFm = null;
		//try {
		    addFm = fm.clone();
		    /*} catch (CloneNotSupportedException e) {
		    e.printStackTrace();
		    }*/
		this.flowTable.addFlowMod(addFm);
		rightChild.flowTable.addGeneratedParentFlowMod(fm, addFm);
		updateTable.addFlowMods.add(addFm);
	    }
	    
	    // delete
	    for (OVXFlowMod fm : leftUpdateTable.deleteFlowMods) {
		List<OVXFlowMod> generatedParentFlowMods = leftChild.flowTable.getGenerateParentFlowMods(fm);
		List<OVXFlowMod> deletedFlowMods = this.flowTable.deleteFlowMods(generatedParentFlowMods);
		updateTable.deleteFlowMods.addAll(deletedFlowMods);
	    }
	    for (OVXFlowMod fm : rightUpdateTable.deleteFlowMods) {
		List<OVXFlowMod> generatedParentFlowMods = rightChild.flowTable.getGenerateParentFlowMods(fm);
		List<OVXFlowMod> deletedFlowMods = this.flowTable.deleteFlowMods(generatedParentFlowMods);
		updateTable.deleteFlowMods.addAll(deletedFlowMods);
	    }
	    leftChild.flowTable.deleteGenerateParentFlowModKeys(leftUpdateTable.deleteFlowMods);
	    rightChild.flowTable.deleteGenerateParentFlowModKeys(rightUpdateTable.deleteFlowMods);
	}
	
	return updateTable;
    }
    
    @Override
    public String toString() {
	String str = null;
	switch (this.operator) {
	case Parallel:
	    str = "(" + this.leftChild + "+" + this.rightChild + ")";
	    break;
	case Sequential:
	    str = "(" + this.leftChild + ">" + this.rightChild + ")";
	    break;
	case Override:
	    str = "(" + this.leftChild + "/" + this.rightChild + ")";
	    break;
	default:
	    //str = tenantId.toString();
	    str = "\n\t" + tenantId.toString() + "\n" + policyACL + "\n" + flowTable;
	    break;
	}
	return str;
    }
	
}
