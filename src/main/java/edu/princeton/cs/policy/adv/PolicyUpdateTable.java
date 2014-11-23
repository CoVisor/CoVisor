package edu.princeton.cs.policy.adv;

import java.util.ArrayList;
import java.util.List;

import org.openflow.protocol.OFFlowMod;

public class PolicyUpdateTable {
	
	public List<OFFlowMod> addFlowMods;
	public List<OFFlowMod> deleteFlowMods;
	
	public PolicyUpdateTable() {
		this.addFlowMods = new ArrayList<OFFlowMod>();
		this.deleteFlowMods = new ArrayList<OFFlowMod>();
	}

	public void addUpdateTable(PolicyUpdateTable partialUpdateTable) {
		this.addFlowMods.addAll(partialUpdateTable.addFlowMods);
		this.deleteFlowMods.addAll(partialUpdateTable.deleteFlowMods);
	}
}
