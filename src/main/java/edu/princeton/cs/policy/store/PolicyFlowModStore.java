package edu.princeton.cs.policy.store;

import java.util.ArrayList;
import java.util.List;

import org.openflow.protocol.OFFlowMod;

public abstract class PolicyFlowModStore {
	
	public enum PolicyFlowModStoreType {
		EXACT,
		PREFIX,
		WILDCARD,
		DISALLOW
	}
	
	public enum PolicyFlowModStoreKey {
		IN_PORT,
		DL_VLAN,
		DL_SRC,
		DL_DST,
		DL_TYPE,
		NW_PROTO,
		TP_SRC,
		TP_DST,
		NW_SRC,
		NW_DST,
		DL_VLAN_PCP,
		NW_TOS,
		ALL
	}
	
	public enum PolicyFlowModAction {
		DataLayerDestination,
		DataLayerSource,
		Enqueue,
		NetworkLayerDestination,
		NetworkLayerSource,
		NetworkTypeOfService,
		Output,
		StripVirtualLan,
		TransportLayerDestination,
		TransportLayerSource,
		Vendor,
		VirtuaLanIdentifier,
		VirtalLanPriorityCodePoint
	}
	
	protected PolicyFlowModStoreType storeType;
	protected PolicyFlowModStoreKey storeKey;
	protected List<PolicyFlowModStoreType> childStoreTypes;
	protected List<PolicyFlowModStoreKey> childStoreKeys;
	protected boolean isLeftInSequentialComposition;
	
	public PolicyFlowModStore(List<PolicyFlowModStoreType> storeTypes,
			List<PolicyFlowModStoreKey> storeKeys,
			Boolean isLeftInSequentialComposition) {
		this.storeType = storeTypes.get(0);
		this.childStoreTypes = new ArrayList<PolicyFlowModStoreType>();
		for (int i = 1; i < storeTypes.size(); i++) {
			this.childStoreTypes.add(storeTypes.get(i));
		}
		
		this.storeKey = storeKeys.get(0);
		this.childStoreKeys = new ArrayList<PolicyFlowModStoreKey>();
		for (int i = 1; i < storeKeys.size(); i++) {
			this.childStoreKeys.add(storeKeys.get(i));
		}
		
		this.isLeftInSequentialComposition = isLeftInSequentialComposition;
	}
	
	@Override
	public String toString() {
		String str = "self-" + this.storeKey + ":" + this.storeType + "\tchildren-";
		for (int i = 0; i < childStoreKeys.size(); i++) {
			str = str + "," + this.childStoreKeys.get(i) + ":" + this.childStoreTypes.get(i);
		}
		return str;
	}

	public abstract void setStore(List<OFFlowMod> flowMods);
	
	public abstract void clear();

	public abstract void add(OFFlowMod fm);

	public abstract OFFlowMod remove(OFFlowMod fm);

	public abstract List<OFFlowMod> removaAll(List<OFFlowMod> flowMods);
	
	public abstract List<OFFlowMod> getFlowMods();

	public abstract List<OFFlowMod> getPotentialFlowMods(OFFlowMod fm);
	
	public static PolicyFlowModStore createFlowModStore(List<PolicyFlowModStoreType> storeTypes,
			List<PolicyFlowModStoreKey> storeKeys,
			Boolean isLeftInSequentialComposition) {
		PolicyFlowModStore flowModStore = null;
		switch (storeTypes.get(0)) {
		case EXACT: {
			switch (storeKeys.get(0)) {
			case DL_SRC:
			case DL_DST:
				flowModStore = new PolicyFlowModStoreMap<ByteArrayWrapper>(storeTypes, storeKeys, isLeftInSequentialComposition);
				break;
			case NW_SRC:
			case NW_DST:
				flowModStore = new PolicyFlowModStoreMap<Integer>(storeTypes, storeKeys, isLeftInSequentialComposition);
				break;
			case DL_VLAN_PCP:
			case NW_PROTO:
			case NW_TOS:
				flowModStore = new PolicyFlowModStoreMap<Byte>(storeTypes, storeKeys, isLeftInSequentialComposition);
				break;
			case IN_PORT:
			case DL_VLAN:
			case DL_TYPE:
			case TP_SRC:
			case TP_DST:
				flowModStore = new PolicyFlowModStoreMap<Short>(storeTypes, storeKeys, isLeftInSequentialComposition);
				break;
			default:
				break;
			}
			break;
		}
		case PREFIX: {
			flowModStore = new PolicyFlowModStoreGoogleTrie(storeTypes, storeKeys, isLeftInSequentialComposition);
			break;
		}
		case WILDCARD: {
			flowModStore = new PolicyFlowModStoreList(storeTypes, storeKeys, isLeftInSequentialComposition);
			break;
		}
		default: {
			break;
		}
		}
		return flowModStore;
	}

}
