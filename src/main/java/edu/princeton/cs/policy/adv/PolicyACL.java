package edu.princeton.cs.policy.adv;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
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

import net.onrc.openvirtex.exceptions.NetworkMappingException;
import edu.princeton.cs.hsa.PlumbingSwitch;
import edu.princeton.cs.hsa.Tuple;
import edu.princeton.cs.policy.adv.PolicyTree.PolicyOperator;
import edu.princeton.cs.policy.store.PolicyFlowModStore.PolicyFlowModStoreKey;
import edu.princeton.cs.policy.store.PolicyFlowModStore.PolicyFlowModStoreType;
import edu.princeton.cs.policy.store.PolicyFlowModStore.PolicyFlowModAction;

public class PolicyACL implements Cloneable {
	
	public Map<PolicyFlowModStoreKey, PolicyFlowModStoreType> aclMatch;
	public Map<PolicyFlowModAction, Boolean> aclAction;
	
	public PolicyACL() {
		this.aclMatch = new HashMap<PolicyFlowModStoreKey, PolicyFlowModStoreType>();
		this.aclAction = new HashMap<PolicyFlowModAction, Boolean>();
		
		for (PolicyFlowModStoreKey field : PolicyFlowModStoreKey.values()) {
			this.aclMatch.put(field, PolicyFlowModStoreType.DISALLOW);
		}
		for (PolicyFlowModAction action : PolicyFlowModAction.values()) {
			this.aclAction.put(action, false);
		}
		
	}
	
	public boolean checkACL (OFFlowMod fm) {
	
		// check match
		OFMatch match = fm.getMatch();
		int wcard = match.getWildcards();
		if ((wcard & OFMatch.OFPFW_IN_PORT) == 0
				&& (this.aclMatch.get(PolicyFlowModStoreKey.IN_PORT) != PolicyFlowModStoreType.EXACT)) {
			return false;
		}

		if ((wcard & OFMatch.OFPFW_DL_VLAN) == 0
				&& (this.aclMatch.get(PolicyFlowModStoreKey.DL_VLAN) != PolicyFlowModStoreType.EXACT)) {
			return false;
		}

		if ((wcard & OFMatch.OFPFW_DL_SRC) == 0
				&& (this.aclMatch.get(PolicyFlowModStoreKey.DL_SRC) != PolicyFlowModStoreType.EXACT)) {
			return false;
		}

		if ((wcard & OFMatch.OFPFW_DL_DST) == 0
				&& (this.aclMatch.get(PolicyFlowModStoreKey.DL_DST) != PolicyFlowModStoreType.EXACT)) {
			return false;
		}

		if ((wcard & OFMatch.OFPFW_DL_TYPE) == 0
				&& (this.aclMatch.get(PolicyFlowModStoreKey.DL_TYPE) != PolicyFlowModStoreType.EXACT)) {
			return false;
		}

		if ((wcard & OFMatch.OFPFW_NW_PROTO) == 0
				&& (this.aclMatch.get(PolicyFlowModStoreKey.NW_PROTO) != PolicyFlowModStoreType.EXACT)) {
			return false;
		}

		if ((wcard & OFMatch.OFPFW_TP_SRC) == 0
				&& (this.aclMatch.get(PolicyFlowModStoreKey.TP_SRC) != PolicyFlowModStoreType.EXACT)) {
			return false;
		}

		if ((wcard & OFMatch.OFPFW_TP_DST) == 0
				&& (this.aclMatch.get(PolicyFlowModStoreKey.TP_DST) != PolicyFlowModStoreType.EXACT)) {
			return false;
		}

		// network source IP
		{
			int mask = wcard & OFMatch.OFPFW_NW_SRC_MASK;
			int shift = Math.min(mask >> OFMatch.OFPFW_NW_SRC_SHIFT, 32);
            if ( !((shift == 0 && this.aclMatch.get(PolicyFlowModStoreKey.NW_SRC) == PolicyFlowModStoreType.EXACT)
                || (shift >= 0 && shift < 32 && this.aclMatch.get(PolicyFlowModStoreKey.NW_SRC) == PolicyFlowModStoreType.PREFIX)
                || shift == 32) ) {
                return false;
			}
        }

		// network destination IP
		{
			int mask = wcard & OFMatch.OFPFW_NW_DST_MASK;
			int shift = Math.min(mask >> OFMatch.OFPFW_NW_DST_SHIFT, 32);
            if ( !((shift == 0 && this.aclMatch.get(PolicyFlowModStoreKey.NW_DST) == PolicyFlowModStoreType.EXACT)
                || (shift >= 0 && shift < 32 && this.aclMatch.get(PolicyFlowModStoreKey.NW_DST) == PolicyFlowModStoreType.PREFIX)
                || shift == 32) ) {
                return false;
			}
		}

		if ((wcard & OFMatch.OFPFW_DL_VLAN_PCP) == 0
				&& (this.aclMatch.get(PolicyFlowModStoreKey.DL_VLAN_PCP) != PolicyFlowModStoreType.EXACT)) {
			return false;
		}

		if ((wcard & OFMatch.OFPFW_NW_TOS) == 0
				&& (this.aclMatch.get(PolicyFlowModStoreKey.NW_TOS) != PolicyFlowModStoreType.EXACT)) {
			return false;
		}

		// check action
		for (OFAction action : fm.getActions()) {

			if (action instanceof OFActionDataLayerDestination
					&& !this.aclAction.get(PolicyFlowModAction.DataLayerDestination)) {
				return false;
			} else if (action instanceof OFActionDataLayerSource
					&& !this.aclAction.get(PolicyFlowModAction.DataLayerSource)) {
				return false;
			} else if (action instanceof OFActionEnqueue
					&& !this.aclAction.get(PolicyFlowModAction.Enqueue)) {
				return false;
			} else if (action instanceof OFActionNetworkLayerDestination
					&& !this.aclAction.get(PolicyFlowModAction.NetworkLayerDestination)) {
				return false;
			} else if (action instanceof OFActionNetworkLayerSource
					&& !this.aclAction.get(PolicyFlowModAction.NetworkLayerSource)) {
				return false;
			} else if (action instanceof OFActionNetworkTypeOfService
					&& !this.aclAction.get(PolicyFlowModAction.NetworkTypeOfService)) {
				return false;
			} else if (action instanceof OFActionOutput
					&& !this.aclAction.get(PolicyFlowModAction.Output)) {
				return false;
			} else if (action instanceof OFActionStripVirtualLan
					&& !this.aclAction.get(PolicyFlowModAction.StripVirtualLan)) {
				return false;
			} else if (action instanceof OFActionTransportLayerDestination
					&& !this.aclAction.get(PolicyFlowModAction.TransportLayerDestination)) {
				return false;
			} else if (action instanceof OFActionTransportLayerSource
					&& !this.aclAction.get(PolicyFlowModAction.TransportLayerSource)) {
				return false;
			} else if (action instanceof OFActionVendor
					&& !this.aclAction.get(PolicyFlowModAction.Vendor)) {
				return false;
			} else if (action instanceof OFActionVirtualLanIdentifier
					&& !this.aclAction.get(PolicyFlowModAction.VirtuaLanIdentifier)) {
				return false;
			} else if (action instanceof OFActionVirtualLanPriorityCodePoint
					&& !this.aclAction.get(PolicyFlowModAction.VirtalLanPriorityCodePoint)) {
				return false;
			}

		}

		return true;
	}
	
	@Override
	public PolicyACL clone() {
        try {
            final PolicyACL ret = (PolicyACL) super.clone();
            ret.aclMatch = new HashMap<PolicyFlowModStoreKey, PolicyFlowModStoreType>();
            ret.aclAction = new HashMap<PolicyFlowModAction, Boolean>();
            for (Map.Entry<PolicyFlowModStoreKey, PolicyFlowModStoreType> entry : this.aclMatch.entrySet()) {
            	ret.aclMatch.put(entry.getKey(), entry.getValue());
            }
            for (Map.Entry<PolicyFlowModAction, Boolean> entry : this.aclAction.entrySet()) {
            	ret.aclAction.put(entry.getKey(), entry.getValue());
            }
            return ret;
        } catch (final CloneNotSupportedException e) {
            throw new RuntimeException(e);
        }
    }
	
	@Override
	public String toString() {
		String str = "";
		for (PolicyFlowModStoreKey field : PolicyFlowModStoreKey.values()) {
            if (this.aclMatch.containsKey(field) && this.aclMatch.get(field) != PolicyFlowModStoreType.DISALLOW) {
			    str = str + field + ":" + this.aclMatch.get(field) + ",";
            }
		}
		str += "\n";
		for (PolicyFlowModAction action : PolicyFlowModAction.values()) {
            if (this.aclAction.containsKey(action) && this.aclAction.get(action)) {
			    str = str + action + ",";
            }
		}
		return str;
	}
	
	public static PolicyACL composeACL (PolicyTree leftChild, PolicyTree rightChild, PolicyOperator operator)
			throws NetworkMappingException {
		
		if (leftChild.policyACL == null) {
			leftChild.initializeFlowTable();
		}
		if (rightChild.policyACL == null) {
			rightChild.initializeFlowTable();
		}
		PolicyACL leftACL = leftChild.policyACL;
		PolicyACL rightACL = rightChild.policyACL;
		PolicyACL policyACL = new PolicyACL();
	
		// generate policy acl
		// deal with match, union
		for (PolicyFlowModStoreKey field : PolicyFlowModStoreKey.values()) {
			if (leftACL.aclMatch.get(field) == PolicyFlowModStoreType.DISALLOW) {
				policyACL.aclMatch.put(field, rightACL.aclMatch.get(field));
			} else if (rightACL.aclMatch.get(field) == PolicyFlowModStoreType.DISALLOW) {
				policyACL.aclMatch.put(field, leftACL.aclMatch.get(field));
			} else if (leftACL.aclMatch.get(field) == PolicyFlowModStoreType.WILDCARD) {
				policyACL.aclMatch.put(field, rightACL.aclMatch.get(field));
			} else if (rightACL.aclMatch.get(field) == PolicyFlowModStoreType.WILDCARD) {
				policyACL.aclMatch.put(field, leftACL.aclMatch.get(field));
			} else if (leftACL.aclMatch.get(field) == PolicyFlowModStoreType.PREFIX) {
				policyACL.aclMatch.put(field, rightACL.aclMatch.get(field));
			} else if (rightACL.aclMatch.get(field) == PolicyFlowModStoreType.PREFIX) {
				policyACL.aclMatch.put(field, leftACL.aclMatch.get(field));
			} else if (leftACL.aclMatch.get(field) == PolicyFlowModStoreType.EXACT) {
				policyACL.aclMatch.put(field, rightACL.aclMatch.get(field));
			} else if (rightACL.aclMatch.get(field) == PolicyFlowModStoreType.EXACT) {
				policyACL.aclMatch.put(field, leftACL.aclMatch.get(field));
			}
		}

		// deal with action, union
		for (PolicyFlowModAction action : PolicyFlowModAction.values()) {
			policyACL.aclAction.put(action, leftACL.aclAction.get(action)
					|| rightACL.aclAction.get(action));
		}

		// generate flow table for children
		if (operator == PolicyOperator.Parallel || operator == PolicyOperator.Sequential) {
			
			if (operator == PolicyOperator.Sequential) {
				leftACL = ACLApplyActToMatch(leftACL);
			}
			
			List<Tuple<PolicyFlowModStoreKey, PolicyFlowModStoreType>> keyTypes =
					new ArrayList<Tuple<PolicyFlowModStoreKey, PolicyFlowModStoreType>>();
			for (PolicyFlowModStoreKey field : PolicyFlowModStoreKey.values()) {
				if (leftACL.aclMatch.get(field) == PolicyFlowModStoreType.DISALLOW
						|| rightACL.aclMatch.get(field) == PolicyFlowModStoreType.DISALLOW) {
					continue;
				} else if (leftACL.aclMatch.get(field) == PolicyFlowModStoreType.WILDCARD
						|| rightACL.aclMatch.get(field) == PolicyFlowModStoreType.WILDCARD) {
					keyTypes.add(new Tuple<PolicyFlowModStoreKey, PolicyFlowModStoreType>(field, PolicyFlowModStoreType.WILDCARD));
				} else if (leftACL.aclMatch.get(field) == PolicyFlowModStoreType.PREFIX
						|| rightACL.aclMatch.get(field) == PolicyFlowModStoreType.PREFIX) {
					keyTypes.add(new Tuple<PolicyFlowModStoreKey, PolicyFlowModStoreType>(field, PolicyFlowModStoreType.PREFIX));
				} else {
					keyTypes.add(new Tuple<PolicyFlowModStoreKey, PolicyFlowModStoreType>(field, PolicyFlowModStoreType.EXACT));
				}
			}
			Collections.sort(keyTypes, new Comparator<Tuple<PolicyFlowModStoreKey, PolicyFlowModStoreType>>() {
				public int compare(Tuple<PolicyFlowModStoreKey, PolicyFlowModStoreType> keyType1,
						Tuple<PolicyFlowModStoreKey, PolicyFlowModStoreType> keyType2) {
					if (keyType1.second == PolicyFlowModStoreType.EXACT) {
						return -1;
					} else if (keyType2.second == PolicyFlowModStoreType.EXACT) {
						return 1;
					} else if (keyType1.second == PolicyFlowModStoreType.PREFIX) {
						return -1;
					} else if (keyType2.second == PolicyFlowModStoreType.PREFIX) {
						return 1;
					} else {
						return 0;
					}
				}
			});
			
			List<PolicyFlowModStoreKey> storeKeys = new ArrayList<PolicyFlowModStoreKey>();
			List<PolicyFlowModStoreType> storeTypes = new ArrayList<PolicyFlowModStoreType>();
			for (Tuple<PolicyFlowModStoreKey, PolicyFlowModStoreType> keyType : keyTypes) {
				storeKeys.add(keyType.first);
				storeTypes.add(keyType.second);
			}
			storeKeys.add(PolicyFlowModStoreKey.ALL);
			storeTypes.add(PolicyFlowModStoreType.WILDCARD);
			if (operator == PolicyOperator.Sequential) {
				leftChild.flowTable = new PolicyFlowTable(storeTypes, storeKeys, true);
			} else {
				leftChild.flowTable = new PolicyFlowTable(storeTypes, storeKeys, false);
			}
			rightChild.flowTable = new PolicyFlowTable(storeTypes, storeKeys, false);
		} else { // override composition
			List<PolicyFlowModStoreKey> storeKeys = new ArrayList<PolicyFlowModStoreKey>();
			List<PolicyFlowModStoreType> storeTypes = new ArrayList<PolicyFlowModStoreType>();
			storeKeys.add(PolicyFlowModStoreKey.ALL);
			storeTypes.add(PolicyFlowModStoreType.WILDCARD);
			leftChild.flowTable = new PolicyFlowTable(storeTypes, storeKeys, false);
			rightChild.flowTable = new PolicyFlowTable(storeTypes, storeKeys, false);
		}
		
		return policyACL;
	}
	
	private static PolicyACL ACLApplyActToMatch (PolicyACL acl) {
		PolicyACL ret = acl.clone();
		for (PolicyFlowModAction action : PolicyFlowModAction.values()) {
			if (acl.aclAction.get(action)) {
				switch (action) {
				case DataLayerDestination:
					ret.aclMatch.put(PolicyFlowModStoreKey.DL_DST, PolicyFlowModStoreType.EXACT);
					break;
				case DataLayerSource:
					ret.aclMatch.put(PolicyFlowModStoreKey.DL_SRC, PolicyFlowModStoreType.EXACT);
					break;
				case NetworkLayerDestination:
					ret.aclMatch.put(PolicyFlowModStoreKey.NW_DST, PolicyFlowModStoreType.EXACT);
					break;
				case NetworkLayerSource:
					ret.aclMatch.put(PolicyFlowModStoreKey.NW_SRC, PolicyFlowModStoreType.EXACT);
					break;
				case TransportLayerDestination:
					ret.aclMatch.put(PolicyFlowModStoreKey.TP_DST, PolicyFlowModStoreType.EXACT);
					break;
				case TransportLayerSource:
					ret.aclMatch.put(PolicyFlowModStoreKey.TP_SRC, PolicyFlowModStoreType.EXACT);
					break;
				default:
					break;
				}
			}
		}
		return ret;
	}

}
