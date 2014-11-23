package edu.princeton.cs.policy.adv;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Random;

import net.onrc.openvirtex.elements.address.PhysicalIPAddress;

import org.openflow.protocol.OFFlowMod;
import org.openflow.protocol.OFMatch;
import org.openflow.protocol.OFPacketOut;
import org.openflow.protocol.action.OFAction;
import org.openflow.protocol.action.OFActionDataLayerDestination;
import org.openflow.protocol.action.OFActionDataLayerSource;
import org.openflow.protocol.action.OFActionNetworkLayerDestination;
import org.openflow.protocol.action.OFActionOutput;
import org.openflow.util.HexString;

public class PolicyCompositionUtil {
	
	public static final short SEQUENTIAL_SHIFT = 8;
	public static final short OVERRIDE_SHIFT = 8;
	
	public static List<OFFlowMod> diffFlowMods (List<OFFlowMod> flowMods1, List<OFFlowMod> flowMods2) {
		List<OFFlowMod> flowModsDiff = new ArrayList<OFFlowMod>();
		for (OFFlowMod fm1 : flowMods1){
			boolean isContained = false;
			for (OFFlowMod fm2 : flowMods2) {
				if (fm1.getMatch().equals(fm2.getMatch()) && fm1.getPriority() == fm2.getPriority()) {
					isContained = true;
					break;
				}
			}
			if (!isContained) {
				flowModsDiff.add(fm1);
			}
		}
		return flowModsDiff;
	}

	public static OFFlowMod parallelComposition(OFFlowMod fm1, OFFlowMod fm2) {
		
		OFFlowMod composedFm = new OFFlowMod();
		composedFm.setCommand(OFFlowMod.OFPFC_ADD);
		composedFm.setIdleTimeout((short)0); // 0 means permanent
		composedFm.setHardTimeout((short)0); // 0 means permanent
		composedFm.setBufferId(OFPacketOut.BUFFER_ID_NONE);
		composedFm.setCookie(0);
		
		// priority
		composedFm.setPriority((short) (fm1.getPriority() + fm2.getPriority()));
		
		// match
		OFMatch match = intersectMatch(fm1.getMatch(), fm2.getMatch());
		if (match != null) {
			composedFm.setMatch(match);
		}
		else {
			return null;
		}
		
		// action
		List<OFAction> actions = new ArrayList<OFAction>();
		int length = OFFlowMod.MINIMUM_LENGTH;
		for (OFAction action : fm1.getActions()) {
			actions.add(action);
			length += action.getLengthU();
		}
		for (OFAction action : fm2.getActions()) {
			actions.add(action);
			length += action.getLengthU();
		}
		composedFm.setActions(actions);
		composedFm.setLengthU(length);
		
		return composedFm;
	}
	
	public static OFFlowMod sequentialComposition(OFFlowMod fm1, OFFlowMod fm2) {
		
		// check fm1 actions, if fwd or drop, stop
		boolean flag = false;
		if (fm1.getActions().isEmpty()) {
			flag = true;
		}
		if (!PolicyTree.ActionOutputAsPass) {
			for (OFAction action : fm1.getActions()) {
				if (action instanceof OFActionOutput) {
					flag = true;
					break;
				}
			}
		}
		if (flag) {
			OFFlowMod composedFm = null;
			try {
				composedFm = fm1.clone();
				composedFm.setPriority(
						(short) (fm1.getPriority() * PolicyCompositionUtil.SEQUENTIAL_SHIFT));
			} catch (CloneNotSupportedException e) {
				e.printStackTrace();
			}
			return composedFm;
		}
		
		// compose logic
		OFFlowMod composedFm = new OFFlowMod();
		composedFm.setCommand(OFFlowMod.OFPFC_ADD);
		composedFm.setIdleTimeout((short)0);
		composedFm.setHardTimeout((short)0);
		composedFm.setBufferId(OFPacketOut.BUFFER_ID_NONE);
		composedFm.setCookie(0);
		
		// priority
		composedFm.setPriority(
				(short) (fm1.getPriority() * PolicyCompositionUtil.SEQUENTIAL_SHIFT + fm2.getPriority()));
		
		// match
		OFMatch match = intersectMatch(fm1.getMatch(), actRevertMatch(fm2.getMatch(), fm1.getActions()));
		if (match != null) {
			composedFm.setMatch(match);
		}
		else {
			return null;
		}
		
		// action
		List<OFAction> actions = new ArrayList<OFAction>();
		int length = OFFlowMod.MINIMUM_LENGTH;
		for (OFAction action : fm1.getActions()) {
			if (PolicyTree.ActionOutputAsPass && action instanceof OFActionOutput) {
				continue;
			}
			actions.add(action);
			length += action.getLengthU();
		}
		for (OFAction action : fm2.getActions()) {
			actions.add(action);
			length += action.getLengthU();
		}
		composedFm.setActions(actions);
		composedFm.setLengthU(length);
		
		return composedFm;
	}
	
	public static OFMatch actApplyMatch(OFMatch match, List<OFAction> actions) {
		OFMatch m = match.clone();
		for (OFAction action : actions) {
			if (action instanceof OFActionNetworkLayerDestination) {
				OFActionNetworkLayerDestination modNwDst = (OFActionNetworkLayerDestination) action;
				m.setWildcards(m.getWildcards() & ~OFMatch.OFPFW_NW_DST_MASK);
				m.setNetworkDestination(modNwDst.getNetworkAddress());
			} else if (action instanceof OFActionDataLayerSource) {
				OFActionDataLayerSource modDataSrc = (OFActionDataLayerSource) action;
				m.setWildcards(m.getWildcards() & ~OFMatch.OFPFW_DL_SRC);
				m.setDataLayerSource(modDataSrc.getDataLayerAddress());
			} else if (action instanceof OFActionDataLayerDestination) {
				OFActionDataLayerDestination modDataDst = (OFActionDataLayerDestination) action;
				m.setWildcards(m.getWildcards() & ~OFMatch.OFPFW_DL_DST);
				m.setDataLayerDestination(modDataDst.getDataLayerAddress());
			}
		}
		return m;
	}
	
	public static OFMatch actRevertMatch(OFMatch match, List<OFAction> actions) {
		OFMatch m = match.clone();
		for (OFAction action : actions) {
			if (action instanceof OFActionNetworkLayerDestination) {
				OFActionNetworkLayerDestination modNwDst = (OFActionNetworkLayerDestination) action;
				int mask = m.getWildcards() & OFMatch.OFPFW_NW_DST_MASK;
				int shift = Math.min(mask >> OFMatch.OFPFW_NW_DST_SHIFT, 32);
				int ip1 = (m.getNetworkDestination() >> shift) << shift;
				int ip2 = (modNwDst.getNetworkAddress() >> shift) << shift;
				if (shift == 32 || ip1 == ip2) {
					m.setWildcards(m.getWildcards() | OFMatch.OFPFW_NW_DST_ALL);
					m.setNetworkDestination(0);
				}
				else {
					return null;
				}
			} else if (action instanceof OFActionDataLayerSource) {
				m.setWildcards(m.getWildcards() | OFMatch.OFPFW_DL_SRC);
				m.setDataLayerSource(HexString.fromHexString("00:00:00:00:00:00"));
			} else if (action instanceof OFActionDataLayerDestination) {
				m.setWildcards(m.getWildcards() | OFMatch.OFPFW_DL_DST);
				m.setDataLayerDestination(HexString.fromHexString("00:00:00:00:00:00"));
			}
		}
		return m;
	}
	
	public static OFMatch intersectMatchIgnoreInport (OFMatch m1, OFMatch m2) {
		if (m1 == null || m2 == null) {
			return null;
		}
		
		OFMatch match = new OFMatch();
		int wcard1 = m1.getWildcards();
		int wcard2 = m2.getWildcards();
		
		match.setWildcards(match.getWildcards() | OFMatch.OFPFW_IN_PORT);
		match.setInputPort((short) 0);
		
		if (!intersectMatchField(match, wcard1, wcard2, OFMatch.OFPFW_DL_VLAN,
				m1.getDataLayerVirtualLan(), m2.getDataLayerVirtualLan())) {
			return null;
		}
		if (!intersectMatchField(match, wcard1, wcard2, OFMatch.OFPFW_DL_SRC,
				m1.getDataLayerSource(), m2.getDataLayerSource())) {
			return null;
		}
		if (!intersectMatchField(match, wcard1, wcard2, OFMatch.OFPFW_DL_DST,
				m1.getDataLayerDestination(), m2.getDataLayerDestination())) {
			return null;
		}
		if (!intersectMatchField(match, wcard1, wcard2, OFMatch.OFPFW_DL_TYPE,
				m1.getDataLayerType(), m2.getDataLayerType())) {
			return null;
		}
		if (!intersectMatchField(match, wcard1, wcard2, OFMatch.OFPFW_NW_PROTO,
				m1.getNetworkProtocol(), m2.getNetworkProtocol())) {
			return null;
		}
		if (!intersectMatchField(match, wcard1, wcard2, OFMatch.OFPFW_TP_SRC,
				m1.getTransportSource(), m2.getTransportSource())) {
			return null;
		}
		if (!intersectMatchField(match, wcard1, wcard2, OFMatch.OFPFW_TP_DST,
				m1.getTransportDestination(), m2.getTransportDestination())) {
			return null;
		}
		
		{
			int mask1 = wcard1 & OFMatch.OFPFW_NW_SRC_MASK;
			int mask2 = wcard2 & OFMatch.OFPFW_NW_SRC_MASK;
			int shift = Math.min(Math.max(mask1, mask2) >> OFMatch.OFPFW_NW_SRC_SHIFT, 32);
			int ip1 = (m1.getNetworkSource() >> shift) << shift;
			int ip2 = (m2.getNetworkSource() >> shift) << shift;
			if (shift == 32 || ip1 == ip2) {
				int wcard = match.getWildcards() & (Math.min(mask1, mask2) | ~OFMatch.OFPFW_NW_SRC_MASK);
				match.setWildcards(wcard);
				
				int ip = mask1 <= mask2 ? m1.getNetworkSource() : m2.getNetworkSource();
				setMatchField(match, OFMatch.OFPFW_NW_SRC_ALL, ip);
			}
			else {
				return null;
			}
		}
		
		{
			int mask1 = wcard1 & OFMatch.OFPFW_NW_DST_MASK;
			int mask2 = wcard2 & OFMatch.OFPFW_NW_DST_MASK;
			int shift = Math.min(Math.max(mask1, mask2) >> OFMatch.OFPFW_NW_DST_SHIFT, 32);
			int ip1 = (m1.getNetworkDestination() >> shift) << shift;
			int ip2 = (m2.getNetworkDestination() >> shift) << shift;
			if (shift == 32 || ip1 == ip2) {
				int wcard = match.getWildcards() & (Math.min(mask1, mask2) | ~OFMatch.OFPFW_NW_DST_MASK);
				match.setWildcards(wcard);
				
				int ip = mask1 <= mask2 ? m1.getNetworkDestination() : m2.getNetworkDestination();
				setMatchField(match, OFMatch.OFPFW_NW_DST_ALL, ip);
			}
			else {
				return null;
			}
		}
		
		if (!intersectMatchField(match, wcard1, wcard2, OFMatch.OFPFW_DL_VLAN_PCP,
				m1.getDataLayerVirtualLanPriorityCodePoint(), m2.getDataLayerVirtualLanPriorityCodePoint())) {
			return null;
		}
		if (!intersectMatchField(match, wcard1, wcard2, OFMatch.OFPFW_NW_TOS,
				m1.getNetworkTypeOfService(), m2.getNetworkTypeOfService())) {
			return null;
		}
		
		return match;
	}

	public static OFMatch intersectMatch (OFMatch m1, OFMatch m2) {
		if (m1 == null || m2 == null) {
			return null;
		}
		
		OFMatch match = new OFMatch();
		int wcard1 = m1.getWildcards();
		int wcard2 = m2.getWildcards();
		
		if (!intersectMatchField(match, wcard1, wcard2, OFMatch.OFPFW_IN_PORT,
				m1.getInputPort(), m2.getInputPort())) {
			return null;
		}
		if (!intersectMatchField(match, wcard1, wcard2, OFMatch.OFPFW_DL_VLAN,
				m1.getDataLayerVirtualLan(), m2.getDataLayerVirtualLan())) {
			return null;
		}
		if (!intersectMatchField(match, wcard1, wcard2, OFMatch.OFPFW_DL_SRC,
				m1.getDataLayerSource(), m2.getDataLayerSource())) {
			return null;
		}
		if (!intersectMatchField(match, wcard1, wcard2, OFMatch.OFPFW_DL_DST,
				m1.getDataLayerDestination(), m2.getDataLayerDestination())) {
			return null;
		}
		if (!intersectMatchField(match, wcard1, wcard2, OFMatch.OFPFW_DL_TYPE,
				m1.getDataLayerType(), m2.getDataLayerType())) {
			return null;
		}
		if (!intersectMatchField(match, wcard1, wcard2, OFMatch.OFPFW_NW_PROTO,
				m1.getNetworkProtocol(), m2.getNetworkProtocol())) {
			return null;
		}
		if (!intersectMatchField(match, wcard1, wcard2, OFMatch.OFPFW_TP_SRC,
				m1.getTransportSource(), m2.getTransportSource())) {
			return null;
		}
		if (!intersectMatchField(match, wcard1, wcard2, OFMatch.OFPFW_TP_DST,
				m1.getTransportDestination(), m2.getTransportDestination())) {
			return null;
		}
		
		{
			int mask1 = wcard1 & OFMatch.OFPFW_NW_SRC_MASK;
			int mask2 = wcard2 & OFMatch.OFPFW_NW_SRC_MASK;
			int shift = Math.min(Math.max(mask1, mask2) >> OFMatch.OFPFW_NW_SRC_SHIFT, 32);
			int ip1 = (m1.getNetworkSource() >> shift) << shift;
			int ip2 = (m2.getNetworkSource() >> shift) << shift;
			if (shift == 32 || ip1 == ip2) {
				int wcard = match.getWildcards() & (Math.min(mask1, mask2) | ~OFMatch.OFPFW_NW_SRC_MASK);
				match.setWildcards(wcard);
				
				int ip = mask1 <= mask2 ? m1.getNetworkSource() : m2.getNetworkSource();
				setMatchField(match, OFMatch.OFPFW_NW_SRC_ALL, ip);
			}
			else {
				return null;
			}
		}
		
		{
			int mask1 = wcard1 & OFMatch.OFPFW_NW_DST_MASK;
			int mask2 = wcard2 & OFMatch.OFPFW_NW_DST_MASK;
			int shift = Math.min(Math.max(mask1, mask2) >> OFMatch.OFPFW_NW_DST_SHIFT, 32);
			int ip1 = (m1.getNetworkDestination() >> shift) << shift;
			int ip2 = (m2.getNetworkDestination() >> shift) << shift;
			if (shift == 32 || ip1 == ip2) {
				int wcard = match.getWildcards() & (Math.min(mask1, mask2) | ~OFMatch.OFPFW_NW_DST_MASK);
				match.setWildcards(wcard);
				
				int ip = mask1 <= mask2 ? m1.getNetworkDestination() : m2.getNetworkDestination();
				setMatchField(match, OFMatch.OFPFW_NW_DST_ALL, ip);
			}
			else {
				return null;
			}
		}
		
		if (!intersectMatchField(match, wcard1, wcard2, OFMatch.OFPFW_DL_VLAN_PCP,
				m1.getDataLayerVirtualLanPriorityCodePoint(), m2.getDataLayerVirtualLanPriorityCodePoint())) {
			return null;
		}
		if (!intersectMatchField(match, wcard1, wcard2, OFMatch.OFPFW_NW_TOS,
				m1.getNetworkTypeOfService(), m2.getNetworkTypeOfService())) {
			return null;
		}
		
		return match;
	}
	
	// deal with Number
	private static boolean intersectMatchField (OFMatch match, int wcard1, int wcard2, int field,
			Number val1, Number val2) {
		int wcard = match.getWildcards();
		if ((wcard1 & field) == 0 && (wcard2 & field) == 0) {
			wcard = wcard & (~field);
			match.setWildcards(wcard);
			if (val1.equals(val2)) {
				setMatchField(match, field, val1);
				return true;
			}
			else {
				return false;
			}
		}
		else if ((wcard1 & field) == 0 && (wcard2 & field) != 0) {
			wcard = wcard & (~field);
			match.setWildcards(wcard);
			setMatchField(match, field, val1);
			return true;
		}
		else if ((wcard1 & field) != 0 && (wcard2 & field) == 0) {
			wcard = wcard & (~field);
			match.setWildcards(wcard);
			setMatchField(match, field, val2);
			return true;
		}
		else if ((wcard1 & field) != 0 && (wcard2 & field) != 0) {
			return true;
		}
		
		return false;
	}
	
	// deal with Number
	private static boolean intersectMatchField(OFMatch match, int wcard1,
			int wcard2, int field, byte[] val1, byte[] val2) {
		int wcard = match.getWildcards();
		if ((wcard1 & field) == 0 && (wcard2 & field) == 0) {
			wcard = wcard & (~field);
			match.setWildcards(wcard);
			/*for (int i = 0; i < MACAddress.MAC_ADDRESS_LENGTH; i++) {
				if (val1[i] != val2[i]) {
					return false;
				}
			}*/
			if (Arrays.equals(val1, val2)) {
				setMatchField(match, field, val1);
				return true;
			}
			else {
				return false;
			}
		} else if ((wcard1 & field) == 0 && (wcard2 & field) != 0) {
			wcard = wcard & (~field);
			match.setWildcards(wcard);
			setMatchField(match, field, val1);
			return true;
		} else if ((wcard1 & field) != 0 && (wcard2 & field) == 0) {
			wcard = wcard & (~field);
			match.setWildcards(wcard);
			setMatchField(match, field, val2);
			return true;
		} else if ((wcard1 & field) != 0 && (wcard2 & field) != 0) {
			return true;
		}

		return false;
	}
	
	private static void setMatchField (OFMatch match, int field, Number val) {
		switch (field) {
		case OFMatch.OFPFW_IN_PORT:
			match.setInputPort((Short) val);
			break;
		case OFMatch.OFPFW_DL_VLAN:
			match.setDataLayerVirtualLan((Short) val);
			break;
		case OFMatch.OFPFW_DL_TYPE:
			match.setDataLayerType((Short) val);
			break;
		case OFMatch.OFPFW_NW_PROTO:
			match.setNetworkProtocol((Byte) val);
			break;
		case OFMatch.OFPFW_TP_SRC:
			match.setTransportSource((Short) val);
			break;
		case OFMatch.OFPFW_TP_DST:
			match.setTransportDestination((Short) val);
			break;
		case OFMatch.OFPFW_NW_SRC_ALL:
			match.setNetworkSource((Integer) val);
			break;
		case OFMatch.OFPFW_NW_DST_ALL:
			match.setNetworkDestination((Integer) val);
			break;
		case OFMatch.OFPFW_DL_VLAN_PCP:
			match.setDataLayerVirtualLanPriorityCodePoint((Byte) val);
			break;
		case OFMatch.OFPFW_NW_TOS:
			match.setNetworkTypeOfService((Byte) val);
			break;
		default:
			break;
		}
	}
	
	private static void setMatchField (OFMatch match, int field, byte[] val) {
		switch (field) {
		case OFMatch.OFPFW_DL_SRC:
			match.setDataLayerSource(val);
			break;
		case OFMatch.OFPFW_DL_DST:
			match.setDataLayerDestination(val);
			break;
		default:
			break;
		}
	}
	
	
	
	/* Example
	 * 
	 * OFFlowMod fm1 = OFFlowModHelper.genFlowMod("priority=1,ether-type=2048,src-ip=1.0.0.0,dst-ip=2.0.0.0,"
	 *	+ "src-mac=00:00:00:00:00:01,dst-mac=00:00:00:00:00:02,src-port=80,dst-port=1,protocol=10");
	 *
	 * OFFlowMod fm2 = OFFlowModHelper.genFlowMod("priority=1,ether-type=2048,src-ip=1.0.0.0/24,dst-ip=2.0.0.0/16,"
	 *	+ "src-mac=00:00:00:00:00:01,dst-mac=00:00:00:00:00:02,src-port=80,dst-port=1,protocol=10,"
	 *	+ "actions=output:1,actions=set-dst-ip:0.0.0.1");
	 */
	public static OFFlowMod genFlowMod (String str) {
		
		OFFlowMod fm = new OFFlowMod();
		fm.setCommand(OFFlowMod.OFPFC_ADD);
		fm.setIdleTimeout((short) 0);
		fm.setHardTimeout((short) 0);
		fm.setBufferId(OFPacketOut.BUFFER_ID_NONE);
		fm.setCookie(0);
		
		OFMatch m = new OFMatch();
		fm.setMatch(m);
		
		List<OFAction> actions = new ArrayList<OFAction>();
		fm.setActions(actions);
		
		int wcards = OFMatch.OFPFW_ALL;
		String[] parts = str.split(",");
		for (String part : parts) {
			
			String[] temp = part.split("=");
			String field = temp[0];
			String value = temp[1];
			
			if (field.equals("priority")) {
				fm.setPriority(Short.parseShort(value));
			} else if (field.equals("inport")) {
				wcards = wcards & ~OFMatch.OFPFW_IN_PORT;
				m.setInputPort(Short.parseShort(value));
			} else if (field.equals("ether-type")) {
				wcards = wcards & ~OFMatch.OFPFW_DL_TYPE;
				m.setDataLayerType(Short.parseShort(value));
			} else if (field.equals("src-mac")) {
				wcards = wcards & ~OFMatch.OFPFW_DL_SRC;
				m.setDataLayerSource(value);
			} else if (field.equals("dst-mac")) {
				wcards = wcards & ~OFMatch.OFPFW_DL_DST;
				m.setDataLayerDestination(value);
			} else if (field.equals("src-ip")) {
				String[] ipPrefix = value.split("/");
				if (ipPrefix.length == 2) {
					String ip = ipPrefix[0];
					int prefix = Integer.parseInt(ipPrefix[1]);
					wcards = wcards & ((32-prefix) << OFMatch.OFPFW_NW_SRC_SHIFT | ~OFMatch.OFPFW_NW_SRC_MASK);
					if (ip.contains(".")) {
						m.setNetworkSource((new PhysicalIPAddress(ip)).getIp());
					} else {
						m.setNetworkSource(Integer.parseInt(ip));
					}
				} else {
					wcards = wcards & ~OFMatch.OFPFW_NW_SRC_MASK;
					if (value.contains(".")) {
						m.setNetworkSource((new PhysicalIPAddress(value)).getIp());
					} else {
						m.setNetworkSource(Integer.parseInt(value));
					}
				}
			} else if (field.equals("dst-ip")) {
				String[] ipPrefix = value.split("/");
				if (ipPrefix.length == 2) {
					String ip = ipPrefix[0];
					int prefix = Integer.parseInt(ipPrefix[1]);
					wcards = wcards & ((32-prefix) << OFMatch.OFPFW_NW_DST_SHIFT | ~OFMatch.OFPFW_NW_DST_MASK);
					if (ip.contains(".")) {
						m.setNetworkDestination((new PhysicalIPAddress(ip)).getIp());
					} else {
						m.setNetworkDestination(Integer.parseInt(ip));
					}
				} else {
					wcards = wcards & ~OFMatch.OFPFW_NW_DST_MASK;
					if (value.contains(".")) {
						m.setNetworkDestination((new PhysicalIPAddress(value)).getIp());
					} else {
						m.setNetworkDestination(Integer.parseInt(value));
					}
				}
			} else if (field.equals("src-port")) {
				wcards = wcards & ~OFMatch.OFPFW_TP_SRC;
				m.setTransportSource(Short.parseShort(value));
			} else if (field.equals("dst-port")) {
				wcards = wcards & ~OFMatch.OFPFW_TP_DST;
				m.setTransportDestination(Short.parseShort(value));
			} else if (field.equals("protocol")) {
				wcards = wcards & ~OFMatch.OFPFW_NW_PROTO;
				m.setNetworkProtocol(Byte.parseByte(value));
			} else if (field.equals("actions")) {
				String actionType = value.split(":")[0];
				String actionValue = value.split(":")[1];
				if (actionType.equals("output")) {
					OFActionOutput action = new OFActionOutput();
					action.setPort(Short.parseShort(actionValue));
					actions.add(action);
				} else if (actionType.equals("set-dst-ip")) {
					OFActionNetworkLayerDestination action = new OFActionNetworkLayerDestination();
					action.setNetworkAddress((new PhysicalIPAddress(actionValue)).getIp());
					actions.add(action);
				} else if (actionType.equals("set-src-mac")) {
					OFActionDataLayerSource action = new OFActionDataLayerSource();
					action.setDataLayerAddress(HexString.fromHexString(value.substring(12)));
					actions.add(action);
				} else if (actionType.equals("set-dst-mac")) {
					OFActionDataLayerDestination action = new OFActionDataLayerDestination();
					action.setDataLayerAddress(HexString.fromHexString(value.substring(12)));
					actions.add(action);
				}
			}
		}
		m.setWildcards(wcards);
		
		int length = OFFlowMod.MINIMUM_LENGTH;
		for (OFAction action : actions) {
			length += action.getLengthU();
		}
		fm.setLengthU(length);
		
		return fm;
	}
	
	public static Random rand = new Random(1);
	// get random number in [min, max)
	public static int getRandomNumber(int min, int max) {
		return rand.nextInt(max - min) + min;
	}
	
}
