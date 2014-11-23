package edu.princeton.cs.policy.store;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.openflow.protocol.OFFlowMod;
import org.openflow.protocol.OFMatch;

public class PolicyFlowModStoreMap<O> extends PolicyFlowModStore {

	private Map<O, PolicyFlowModStore> flowModsMap;
	private O wildcardKey;
	
	public PolicyFlowModStoreMap(List<PolicyFlowModStoreType> storeTypes,
			List<PolicyFlowModStoreKey> storeKeys,
			Boolean isLeftInSequentialComposition) {
		super(storeTypes, storeKeys, isLeftInSequentialComposition);
		this.flowModsMap = new HashMap<O, PolicyFlowModStore>();
		this.wildcardKey = generateWildcardKey();
	}
	
	@Override
	public void setStore(List<OFFlowMod> flowMods) {
		this.clear();
		for (OFFlowMod fm : flowMods) {
			this.add(fm);
		}
	}

	@Override
	public void clear() {
		this.flowModsMap.clear();
	}

	@Override
	public void add(OFFlowMod fm) {
		O key = this.getKey(fm);
		PolicyFlowModStore value = this.flowModsMap.get(key);
		if (value == null) {
			value = PolicyFlowModStore.createFlowModStore(this.childStoreTypes, this.childStoreKeys, this.isLeftInSequentialComposition);
			this.flowModsMap.put(key, value);
		}
		value.add(fm);
	}
	
	@SuppressWarnings("unchecked")
	private O getKey (OFFlowMod fm) {
		
		OFMatch match = null;
		if (this.isLeftInSequentialComposition) {
			match = fm.getActApplyMatch();
		} else {
			match = fm.getMatch();
		}
		
		O key = null;
		switch (this.storeKey) {
		case IN_PORT:
			key = (O) Short.valueOf(match.getInputPort());
			break;
		case DL_VLAN:
			key = (O) Short.valueOf(match.getDataLayerVirtualLan());
			break;
		case DL_SRC:
			key = (O) new ByteArrayWrapper(match.getDataLayerSource());
			break;
		case DL_DST:
			key = (O) new ByteArrayWrapper(match.getDataLayerDestination());
			break;
		case DL_TYPE:
			key = (O) Short.valueOf(match.getDataLayerType());
			break;
		case NW_PROTO:
			key = (O) Byte.valueOf(match.getNetworkProtocol());
			break;
		case TP_SRC:
			key = (O) Short.valueOf(match.getTransportSource());
			break;
		case TP_DST:
			key = (O) Short.valueOf(match.getTransportDestination());
			break;
		case NW_SRC:
			key = (O) Integer.valueOf(match.getNetworkSource());
			break;
		case NW_DST:
			key = (O) Integer.valueOf(match.getNetworkDestination());
			break;
		case DL_VLAN_PCP:
			key = (O) Byte.valueOf(match.getDataLayerVirtualLanPriorityCodePoint());
			break;
		case NW_TOS:
			key = (O) Byte.valueOf(match.getNetworkTypeOfService());
			break;
		default:
			break;
		}
		return key;
	}
	
	@SuppressWarnings("unchecked")
	private O generateWildcardKey () {
		O key = null;
		switch (this.storeKey) {
		case IN_PORT:
			key = (O) Short.valueOf((short) 0);
			break;
		case DL_VLAN:
			key = (O) Short.valueOf((short) 0);
			break;
		case DL_SRC:
			key = (O) new ByteArrayWrapper(new byte[] {0x00, 0x00, 0x00, 0x00, 0x00, 0x00});
			break;
		case DL_DST:
			key = (O) new ByteArrayWrapper(new byte[] {0x00, 0x00, 0x00, 0x00, 0x00, 0x00});
			break;
		case DL_TYPE:
			key = (O) Short.valueOf((short) 0);
			break;
		case NW_PROTO:
			key = (O) Byte.valueOf((byte) 0);
			break;
		case TP_SRC:
			key = (O) Short.valueOf((short) 0);
			break;
		case TP_DST:
			key = (O) Short.valueOf((short) 0);
			break;
		case NW_SRC:
			key = (O) Integer.valueOf(0);
			break;
		case NW_DST:
			key = (O) Integer.valueOf(0);
			break;
		case DL_VLAN_PCP:
			key = (O) Byte.valueOf((byte) 0);
			break;
		case NW_TOS:
			key = (O) Byte.valueOf((byte) 0);
			break;
		default:
			break;
		}
		return key;
	}

	@Override
	public OFFlowMod remove(OFFlowMod fm) {
		O key = this.getKey(fm);
		PolicyFlowModStore value = this.flowModsMap.get(key);
		if (value != null) {
			return value.remove(fm);
		} else {
			return null;
		}
	}

	@Override
	public List<OFFlowMod> removaAll(List<OFFlowMod> flowMods) {
		List<OFFlowMod> deletedFms = new ArrayList<OFFlowMod>();
		for (OFFlowMod fm : flowMods) {
			O key = this.getKey(fm);
			PolicyFlowModStore value = this.flowModsMap.get(key);
			if (value != null) {
				OFFlowMod deleted = value.remove(fm);
				if (deleted != null) {
					deletedFms.add(deleted);
				}
			}
		}
		return deletedFms;
	}

	@Override
	public List<OFFlowMod> getFlowMods() {
		List<OFFlowMod> flowMods = new ArrayList<OFFlowMod>();
		for (PolicyFlowModStore flowModStore : this.flowModsMap.values()) {
			flowMods.addAll(flowModStore.getFlowMods());
		}
		return flowMods;
	}

	@Override
	public List<OFFlowMod> getPotentialFlowMods(OFFlowMod fm) {
		O key = this.getKey(fm);
		if (key.equals(wildcardKey)) {
			return this.getFlowMods();
		} else {
			List<OFFlowMod> potentialFlowMods = new ArrayList<OFFlowMod>();
			
			// get flowmods that match this field
			PolicyFlowModStore value = this.flowModsMap.get(key);
			if (value != null) {
				potentialFlowMods.addAll(value.getPotentialFlowMods(fm));
			}

			// get flowmods that wildcard this field
			value = this.flowModsMap.get(this.wildcardKey);
			if (value != null) {
				potentialFlowMods.addAll(value.getPotentialFlowMods(fm));
			}
			
			return potentialFlowMods;
		}
	}
}
