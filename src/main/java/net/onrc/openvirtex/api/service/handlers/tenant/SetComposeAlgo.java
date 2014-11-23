package net.onrc.openvirtex.api.service.handlers.tenant;

import java.util.Map;
import java.util.Map.Entry;
import java.util.concurrent.ConcurrentHashMap;

import net.onrc.openvirtex.api.service.handlers.ApiHandler;
import net.onrc.openvirtex.elements.OVXMap;
import net.onrc.openvirtex.elements.datapath.OVXSwitch;
import net.onrc.openvirtex.elements.datapath.PhysicalSwitch;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import com.thetransactioncompany.jsonrpc2.JSONRPC2ParamsType;
import com.thetransactioncompany.jsonrpc2.JSONRPC2Response;

import edu.princeton.cs.policy.adv.PolicyTree;

public class SetComposeAlgo extends ApiHandler<Map<String, Object>> {

	private Logger log = LogManager.getLogger(SetComposeAlgo.class.getName());
	
	@Override
	public JSONRPC2Response process(final Map<String, Object> params) {
		
		final OVXMap map = OVXMap.getInstance();
		/*for (PhysicalSwitch sw : map.getPhysicalSwitchMap().keySet()) {
			this.log.info("enter expr");
			sw.runExpr();
		}
		for (Entry<PhysicalSwitch, ConcurrentHashMap<Integer, OVXSwitch>> entry
				: map.getPhysicalSwitchMap().entrySet()) {
			for (Entry<Integer, OVXSwitch> subEntry : entry.getValue().entrySet()) {
				if (subEntry.getValue() instanceof OVXMultiSwitch) {
					this.log.info("enter expr");
					((OVXMultiSwitch) subEntry.getValue()).runExpr();
				}
			}
		}
		

		final String algo = (String) params.get("algo");
		if (algo.equals("strawman")) {
			PolicyTree.UPDATEMECHANISM = PolicyUpdateMechanism.Strawman;
		} else {
			PolicyTree.UPDATEMECHANISM = PolicyUpdateMechanism.Incremental;
		}
		
		this.log.info("set compose algorithm to {}", PolicyTree.UPDATEMECHANISM);
		this.log.info("MagicTimestamp\t4\t{}", System.nanoTime());*/
		return new JSONRPC2Response(0);
	}

	@Override
	public JSONRPC2ParamsType getType() {
		return JSONRPC2ParamsType.OBJECT;
	}

}
