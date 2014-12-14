package edu.princeton.cs.hsa;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import java.util.Map;

import org.openflow.protocol.OFFlowMod;
import org.openflow.protocol.OFMatch;
import org.openflow.protocol.action.OFAction;
import org.openflow.protocol.action.OFActionNetworkLayerDestination;
import org.openflow.protocol.action.OFActionOutput;

import edu.princeton.cs.policy.adv.PolicyCompositionUtil;
import net.onrc.openvirtex.messages.OVXFlowMod;

public class PlumbingFlowMod extends OVXFlowMod {
	
    private OVXFlowMod originalOfm;
    // FlowMods derived from this PlumbingFlowMod.
    private List<OVXFlowMod> childrenFlowMods;
    
    private List<PlumbingFlowMod> prevPmods;
    private List<PlumbingFlowMod> nextPmods;
    private List<PlumbingFlow> prevPflows;
    private List<PlumbingFlow> nextPflows;
    private PlumbingSwitch pNode;
    
    public PlumbingFlowMod(final OVXFlowMod fm, final PlumbingSwitch pNode) {
	super();
	this.match = fm.getMatch();
	this.cookie = fm.getCookie();
	this.command = fm.getCommand();
	this.idleTimeout = fm.getIdleTimeout();
	this.hardTimeout = fm.getHardTimeout();
	this.priority = fm.getPriority();
	this.bufferId = fm.getBufferId();
	this.outPort = fm.getOutPort();
	this.flags = fm.getFlags();
	this.actions = fm.getActions();
	
	// Pointer to flow mod from table stored at root of PolicyTree.
	this.originalOfm = fm;
	this.prevPmods = new ArrayList<PlumbingFlowMod>();
	this.nextPmods = new ArrayList<PlumbingFlowMod>();
	this.prevPflows = new ArrayList<PlumbingFlow>();
	this.nextPflows = new ArrayList<PlumbingFlow>();
	this.pNode = pNode;

	addChildFlowMod(fm);
    }
    
    public void createFilter(PlumbingFlowMod nextPmod) {
	OFMatch thisMatch = this.getMatch().clone();
	thisMatch.setWildcards(thisMatch.getWildcards() & ~OFMatch.OFPFW_IN_PORT);
	thisMatch.setInputPort(this.pNode.getNextHopPort(this));
	
	OFMatch match = PolicyCompositionUtil.intersectMatch(thisMatch,
							     PolicyCompositionUtil.actRevertMatch(nextPmod.getMatch(), this.getActions()));
	if(match != null) {
	    this.nextPmods.add(nextPmod);
	    nextPmod.prevPmods.add(this);
	}
    }
    
    public Collection<PlumbingFlowMod> getPrevPMods() {
	return this.prevPmods;
    }
    
    public Collection<PlumbingFlowMod> getNextPMods() {
	return this.nextPmods;
    }
    
    public Collection<PlumbingFlow> getPrevPFlows() {
	return this.prevPflows;
    }
    
    public Collection<PlumbingFlow> getNextPFlows() {
	return this.nextPflows;
    }
    
    public void addPrevPFlow(PlumbingFlow pflow) {
	this.prevPflows.add(pflow);
    }
    
    public void addNextPFlow(PlumbingFlow pflow) {
	this.nextPflows.add(pflow);
    }
    
    public OVXFlowMod getOriginalOfm() {
	return this.originalOfm;
    }
	
    public PlumbingSwitch getPlumbingNode () {
	return this.pNode;
    }

}
