package net.onrc.openvirtex.api.service.handlers.tenant;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.concurrent.ConcurrentHashMap;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import com.thetransactioncompany.jsonrpc2.JSONRPC2Error;
import com.thetransactioncompany.jsonrpc2.JSONRPC2ParamsType;
import com.thetransactioncompany.jsonrpc2.JSONRPC2Response;

import edu.princeton.cs.hsa.PlumbingSwitch;
import edu.princeton.cs.policy.adv.PolicyParseUtil;
import edu.princeton.cs.policy.adv.PolicyTree;
import edu.princeton.cs.policy.adv.PolicyTree.PolicyOperator;
import edu.princeton.cs.policy.store.PolicyFlowModStore.PolicyFlowModStoreKey;
import edu.princeton.cs.policy.store.PolicyFlowModStore.PolicyFlowModStoreType;
import net.onrc.openvirtex.api.service.handlers.ApiHandler;
import net.onrc.openvirtex.api.service.handlers.HandlerUtils;
import net.onrc.openvirtex.api.service.handlers.TenantHandler;
import net.onrc.openvirtex.elements.OVXMap;
import net.onrc.openvirtex.elements.datapath.OVXSwitch;
import net.onrc.openvirtex.elements.datapath.PhysicalSwitch;
import net.onrc.openvirtex.elements.network.PhysicalNetwork;
import net.onrc.openvirtex.exceptions.MissingRequiredField;

public class CreatePolicy extends ApiHandler<Map<String, Object>> {

	private Logger log = LogManager.getLogger(CreatePolicy.class.getName());
	
	@Override
	public JSONRPC2Response process(final Map<String, Object> params) {
		JSONRPC2Response resp = null;
		try {
			final Long dpid = HandlerUtils.<Number> fetchField(TenantHandler.DPID,
					params, true, null).longValue();
			final Integer plumbingSwitchId = HandlerUtils.<Number> fetchField(
					TenantHandler.PLUMBING_SWITCH_ID, params, true, null).intValue();
			final String policy = HandlerUtils.<String> fetchField(
					TenantHandler.POLICY, params, true, null);
			
			PolicyTree policyTree = PolicyParseUtil.parsePolicyString(policy);
			
			final PhysicalSwitch physicalSwitch = PhysicalNetwork.getInstance().getSwitch(dpid);
			final PlumbingSwitch plumbingSwitch = physicalSwitch.getPlumbingGraph().getNode(plumbingSwitchId);
			plumbingSwitch.setPolicyTree(policyTree);
			
		} catch (Exception e) {
			resp = new JSONRPC2Response(new JSONRPC2Error(
                    JSONRPC2Error.INVALID_PARAMS.getCode(), this.cmdName()
                            + e.getMessage()), 0);
			this.log.info(e.getMessage());
		}
    	
		// install policy
		/*final OVXMap map = OVXMap.getInstance();
		for (Entry<PhysicalSwitch, ConcurrentHashMap<Integer, OVXSwitch>> entry
				: map.getPhysicalSwitchMap().entrySet()) {
			
			PolicyTree policyTree = new PolicyTree();
			policyTree.operator = policyOperator;
			
			PhysicalSwitch sw = entry.getKey();
			for (Entry<Integer, OVXSwitch> tenantSw : entry.getValue().entrySet()) {
				PolicyTree subPolicyTree = new PolicyTree(storeTypes, storeKeys);
				subPolicyTree.tenantId = tenantSw.getKey();
				//if (policyTree.leftChild == null) {
				if (subPolicyTree.tenantId == 1) {
					policyTree.leftChild = subPolicyTree;
				}
				else {
					policyTree.rightChild = subPolicyTree;
				}
			}
			//sw.ConfigurePolicy(policyTree);

		}*/
		
        resp = new JSONRPC2Response(0);
		return resp;
	}

	@Override
	public JSONRPC2ParamsType getType() {
		return JSONRPC2ParamsType.OBJECT;
	}

}
