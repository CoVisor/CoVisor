package edu.princeton.cs.policy.adv;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.concurrent.ConcurrentHashMap;

import org.apache.commons.lang.NotImplementedException;
import org.openflow.protocol.OFFlowMod;
import org.openflow.protocol.OFMatch;
import org.openflow.protocol.action.OFAction;
import org.openflow.protocol.action.OFActionDataLayerDestination;
import org.openflow.protocol.action.OFActionDataLayerSource;
import org.openflow.protocol.action.OFActionEnqueue;
import org.openflow.protocol.action.OFActionNetworkLayerDestination;
import org.openflow.protocol.action.OFActionNetworkLayerSource;
import org.openflow.protocol.action.OFActionNetworkTypeOfService;
import org.openflow.protocol.action.OFActionOutput;
import org.openflow.protocol.action.OFActionStripVirtualLan;
import org.openflow.protocol.action.OFActionTransportLayerDestination;
import org.openflow.protocol.action.OFActionTransportLayerSource;
import org.openflow.protocol.action.OFActionVendor;
import org.openflow.protocol.action.OFActionVirtualLanIdentifier;
import org.openflow.protocol.action.OFActionVirtualLanPriorityCodePoint;

import edu.princeton.cs.policy.store.PolicyFlowModStore;
import edu.princeton.cs.policy.store.PolicyFlowModStore.PolicyFlowModStoreKey;
import edu.princeton.cs.policy.store.PolicyFlowModStore.PolicyFlowModStoreType;

import net.onrc.openvirtex.messages.OVXFlowMod;

public class PolicyFlowTable {

    private ConcurrentHashMap<OVXFlowMod, List<OVXFlowMod>>
	generatedParentFlowModsDictionary;
    private PolicyFlowModStore flowModStore;
    
    public PolicyFlowTable() {
	this.generatedParentFlowModsDictionary =
	    new ConcurrentHashMap<OVXFlowMod, List<OVXFlowMod>>();
	
	List<PolicyFlowModStoreType> storeTypes = new ArrayList<PolicyFlowModStoreType>();
	storeTypes.add(PolicyFlowModStoreType.WILDCARD);
    	List<PolicyFlowModStoreKey> storeKeys = new ArrayList<PolicyFlowModStoreKey>();
    	storeKeys.add(PolicyFlowModStoreKey.ALL);
    	this.flowModStore = PolicyFlowModStore.createFlowModStore(storeTypes, storeKeys, false);
    }
    
    public PolicyFlowTable(List<PolicyFlowModStoreType> storeTypes,
			   List<PolicyFlowModStoreKey> storeKeys,
			   boolean isLeftInSequentialComposition) {
	this.generatedParentFlowModsDictionary =
	    new ConcurrentHashMap<OVXFlowMod, List<OVXFlowMod>>();
	this.flowModStore = PolicyFlowModStore.
	    createFlowModStore(storeTypes, storeKeys, isLeftInSequentialComposition);
    }
    
    public void addFlowMod(OVXFlowMod fm) {
	this.flowModStore.add(fm);
	this.generatedParentFlowModsDictionary.put(fm, new ArrayList<OVXFlowMod>());
    }
	
    public void setTable(List<OVXFlowMod> flowMods) {
	this.flowModStore.setStore(flowMods);
    }
    
    public void clearTable() {
	this.flowModStore.clear();
    }
    
    public PolicyUpdateTable update (OVXFlowMod fm) {
	switch (fm.getCommand()) {
        case OFFlowMod.OFPFC_ADD:
            return doFlowModAdd(fm);
        case OFFlowMod.OFPFC_MODIFY:
        case OFFlowMod.OFPFC_MODIFY_STRICT:
            throw new NotImplementedException("don't allow OFPFC_MODIFY and OFPFC_MODIFY_STRICT");
        case OFFlowMod.OFPFC_DELETE:
        case OFFlowMod.OFPFC_DELETE_STRICT:
            return doFlowModDelete(fm);
        default:
            return null;
        }
    }
    
    private PolicyUpdateTable doFlowModAdd(OVXFlowMod fm) {
	this.addFlowMod(fm);
	
	PolicyUpdateTable updateTable = new PolicyUpdateTable();
	updateTable.addFlowMods.add(fm);
	System.out.println(updateTable);
	return updateTable;
    }
    
    private PolicyUpdateTable doFlowModDelete(OVXFlowMod fm) {
	OVXFlowMod deletedFm = this.flowModStore.remove(fm);
	
	PolicyUpdateTable updateTable = new PolicyUpdateTable();
	if (deletedFm != null) {
	    updateTable.deleteFlowMods.add(deletedFm);
	}
	System.out.println(updateTable);
	return updateTable;
    }
    
    public List<OVXFlowMod> getFlowMods() {
	return this.flowModStore.getFlowMods();
    }
	
    public List<OVXFlowMod> getFlowModsSorted() {
	List<OVXFlowMod> flowMods = this.flowModStore.getFlowMods();
	Collections.sort(flowMods, new Comparator<OVXFlowMod>() {
		public int compare(OVXFlowMod fm1, OVXFlowMod fm2) {
		    return fm2.getPriority() - fm1.getPriority();
		}
	    });
	return flowMods;
    }
    
    public List<OVXFlowMod> getFlowModsSortByInport() {
	List<OVXFlowMod> flowMods = this.flowModStore.getFlowMods();
	Collections.sort(flowMods, new Comparator<OVXFlowMod>() {
		public int compare(OVXFlowMod fm1, OVXFlowMod fm2) {
		    if (fm1.getMatch().getInputPort() != fm2.getMatch().getInputPort()) {
			return fm1.getMatch().getInputPort() - fm2.getMatch().getInputPort();
		    } else {
			return fm2.getPriority() - fm1.getPriority();
		    }
		}
	    });
	return flowMods;
    }
    
    @Override
    public String toString() {
	String str = "Flow Table\t" + this.flowModStore + "\n";
	for (OVXFlowMod fm : this.flowModStore.getFlowMods()) {
	    str = str + fm.toString() + "\n";
	}
	return str;
    }
    
    public List<OVXFlowMod> getGenerateParentFlowMods(OVXFlowMod fm) {
	return this.generatedParentFlowModsDictionary.get(fm);
    }
    
    public List<OVXFlowMod> deleteFlowMods(List<OVXFlowMod> flowMods) {
	return this.flowModStore.removaAll(flowMods);
    }
	
    public void addGeneratedParentFlowMod (OVXFlowMod fm,
					   OVXFlowMod generateParentFlowMod) {
	this.generatedParentFlowModsDictionary.get(fm).add(generateParentFlowMod);
    }
    
    public void deleteGenerateParentFlowModKey (OVXFlowMod fm) {
	this.generatedParentFlowModsDictionary.remove(fm);
    }
    
    public void deleteGenerateParentFlowModKeys (List<OVXFlowMod> fms) {
	for (OVXFlowMod fm : fms) {
	    this.deleteGenerateParentFlowModKey(fm);
	}
    }
    
    public List<OVXFlowMod> getPotentialFlowMods (OVXFlowMod fm) {
	return this.flowModStore.getPotentialFlowMods(fm);
    }
}
