package edu.princeton.cs.policy.store;

import java.util.ArrayList;
import java.util.List;

import org.openflow.protocol.OFFlowMod;
import org.openflow.protocol.OFMatch;
import net.onrc.openvirtex.messages.OVXFlowMod;

import edu.princeton.cs.iptrie.IPTrie;
import edu.princeton.cs.policy.store.PolicyFlowModStore.PolicyFlowModStoreKey;
import edu.princeton.cs.policy.store.PolicyFlowModStore.PolicyFlowModStoreType;


public class PolicyFlowModStoreTrie extends PolicyFlowModStore {
	
	private IPTrie<PolicyFlowModStore> flowModsTrie;
	private PolicyFlowModStore wildcardFlowStore;
	
	public PolicyFlowModStoreTrie(List<PolicyFlowModStoreType> storeTypes,
			List<PolicyFlowModStoreKey> storeKeys,
			Boolean isLeftInSequentialComposition) {
		super(storeTypes, storeKeys, isLeftInSequentialComposition);
		this.flowModsTrie = new IPTrie<PolicyFlowModStore>();
		
		List<PolicyFlowModStoreType> wildcardStoreTypes = new ArrayList<PolicyFlowModStoreType>();
		wildcardStoreTypes.add(PolicyFlowModStoreType.WILDCARD);
    	List<PolicyFlowModStoreKey> wildcardStoreKeys = new ArrayList<PolicyFlowModStoreKey>();
    	wildcardStoreKeys.add(PolicyFlowModStoreKey.ALL);
		this.wildcardFlowStore = new PolicyFlowModStoreList(wildcardStoreTypes, wildcardStoreKeys, isLeftInSequentialComposition);
	}

	@Override
	public void setStore(List<OVXFlowMod> flowMods) {
		this.clear();
		for (OVXFlowMod fm : flowMods) {
			this.add(fm);
		}
	}

	@Override
	public void clear() {
		this.flowModsTrie = new IPTrie<PolicyFlowModStore>();
		this.wildcardFlowStore.clear();
	}

	@Override
	public void add(OVXFlowMod fm) {
		String key = this.getKey(fm);
		if (key.equals("")) {
			this.wildcardFlowStore.add(fm);
		} else {
			PolicyFlowModStore value = this.flowModsTrie.getExact(key);
			if (value == null) {
				value = PolicyFlowModStore.createFlowModStore(
						this.childStoreTypes, this.childStoreKeys, this.isLeftInSequentialComposition);
				this.flowModsTrie.put(key, value);
			}
			value.add(fm);
		}
	}
	
	private String getKey (OVXFlowMod fm) {
		
		OFMatch match = null;
		if (this.isLeftInSequentialComposition) {
			match = fm.getActApplyMatch();
		} else {
			match = fm.getMatch();
		}
		
		int ip = 0;
		int prefixLen = 0;
		switch (this.storeKey) {
		case NW_SRC:
			ip = match.getNetworkSource();
			prefixLen = match.getNetworkSourceMaskLen(); 
			break;
		case NW_DST:
			ip = match.getNetworkDestination();
			prefixLen = match.getNetworkDestinationMaskLen();
			break;
		default:
			break;
		}
		return String.format("%32s", Integer.toBinaryString(ip)).replace(' ', '0').substring(0, prefixLen);
	}

	@Override
	public OVXFlowMod remove(OVXFlowMod fm) {
		String key = this.getKey(fm);
		if (key.equals("")) {
			return wildcardFlowStore.remove(fm);
		} else {
			PolicyFlowModStore value = this.flowModsTrie.getExact(key);
			if (value != null) {
				return value.remove(fm);
			}
		}
		return null;
	}

	@Override
	public List<OVXFlowMod> removaAll(List<OVXFlowMod> flowMods) {
		List<OVXFlowMod> deletedFms = new ArrayList<OVXFlowMod>();
		for (OVXFlowMod fm : flowMods) {
			String key = this.getKey(fm);
			if (key.equals("")) {
				OVXFlowMod deleted =wildcardFlowStore.remove(fm);
				if (deleted != null) {
					deletedFms.add(deleted);
				}
			} else {
				PolicyFlowModStore value = this.flowModsTrie.getExact(key);
				if (value != null) {
					OVXFlowMod deleted = value.remove(fm);
					if (deleted != null) {
						deletedFms.add(deleted);
					}
				}
			}
		}
		return deletedFms;
	}

	@Override
	public List<OVXFlowMod> getFlowMods() {
		List<OVXFlowMod> flowMods = new ArrayList<OVXFlowMod>();

		// get flowmods that match this field
		List<PolicyFlowModStore> values = this.flowModsTrie.get("");
		for (PolicyFlowModStore value : values) {
			flowMods.addAll(value.getFlowMods());
		}

		// get flowmods that wildcard this field
		flowMods.addAll(this.wildcardFlowStore.getFlowMods());
		return flowMods;
	}

	@Override
	public List<OVXFlowMod> getPotentialFlowMods(OVXFlowMod fm) {
		String key = this.getKey(fm);

		List<OVXFlowMod> flowMods = new ArrayList<OVXFlowMod>();

		// get flowmods that match this field
		List<PolicyFlowModStore> values = this.flowModsTrie.get(key);
		for (PolicyFlowModStore value : values) {
			flowMods.addAll(value.getPotentialFlowMods(fm));
		}

		// get flowmods that wildcard this field
		flowMods.addAll(this.wildcardFlowStore.getFlowMods());
		return flowMods;
	}
}
