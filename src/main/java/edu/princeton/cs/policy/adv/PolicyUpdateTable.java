package edu.princeton.cs.policy.adv;

import java.util.ArrayList;
import java.util.List;

import org.openflow.protocol.OFFlowMod;
import net.onrc.openvirtex.messages.OVXFlowMod;

public class PolicyUpdateTable {
	
    public List<OVXFlowMod> addFlowMods;
    public List<OVXFlowMod> deleteFlowMods;
    
    public PolicyUpdateTable() {
	this.addFlowMods = new ArrayList<OVXFlowMod>();
	this.deleteFlowMods = new ArrayList<OVXFlowMod>();
    }
    
    public void addUpdateTable(PolicyUpdateTable partialUpdateTable) {
	this.addFlowMods.addAll(partialUpdateTable.addFlowMods);
	this.deleteFlowMods.addAll(partialUpdateTable.deleteFlowMods);
    }
}
