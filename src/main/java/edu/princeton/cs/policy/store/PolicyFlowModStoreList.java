package edu.princeton.cs.policy.store;

import java.util.ArrayList;
import java.util.List;

import org.openflow.protocol.OFFlowMod;
import net.onrc.openvirtex.messages.OVXFlowMod;

public class PolicyFlowModStoreList extends PolicyFlowModStore {
	
	private List<OVXFlowMod> flowMods;
	
	public PolicyFlowModStoreList (List<PolicyFlowModStoreType> storeTypes,
			List<PolicyFlowModStoreKey> storeKeys,
			Boolean isLeftInSequentialComposition) {
		super(storeTypes, storeKeys, isLeftInSequentialComposition);
		this.flowMods = new ArrayList<OVXFlowMod>();
	}

	@Override
	public void setStore(List<OVXFlowMod> flowMods) {
		this.flowMods = flowMods;
	}

	@Override
	public void clear() {
		this.flowMods.clear();
	}

	@Override
	public void add(OVXFlowMod fm) {
		this.flowMods.add(fm);
	}

	@Override
	public OVXFlowMod remove(OVXFlowMod fm) {
		OVXFlowMod toDelete = null;
		for (OVXFlowMod curFlowMod : this.flowMods) {
			if (curFlowMod.getMatch().equals(fm.getMatch()) && curFlowMod.getPriority() == fm.getPriority()) {
				toDelete = curFlowMod;
				break;
			}
		}
		if (toDelete != null) {
			this.flowMods.remove(toDelete);
		}
		return toDelete;
	}

	@Override
	public List<OVXFlowMod> removaAll(List<OVXFlowMod> flowMods) {
		List<OVXFlowMod> toDelete = new ArrayList<OVXFlowMod>();
		for (OVXFlowMod fm : flowMods) {
			for (OVXFlowMod curFlowMod : this.flowMods) {
				if (curFlowMod.getMatch().equals(fm.getMatch()) && curFlowMod.getPriority() == fm.getPriority()) {
					toDelete.add(curFlowMod);
					break;
				}
			}
		}
		this.flowMods.removeAll(toDelete);
		return toDelete;
	}

	@Override
	public List<OVXFlowMod> getFlowMods() {
		return this.flowMods;
	}

	@Override
	public List<OVXFlowMod> getPotentialFlowMods(OVXFlowMod fm) {
		return this.flowMods;
	}

}
