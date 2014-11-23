package net.onrc.openvirtex.api.service.handlers.tenant;

import java.util.Map;

import net.onrc.openvirtex.api.service.handlers.ApiHandler;
import net.onrc.openvirtex.api.service.handlers.HandlerUtils;
import net.onrc.openvirtex.api.service.handlers.TenantHandler;
import net.onrc.openvirtex.elements.datapath.PhysicalSwitch;
import net.onrc.openvirtex.elements.network.PhysicalNetwork;
import net.onrc.openvirtex.exceptions.MissingRequiredField;

import com.thetransactioncompany.jsonrpc2.JSONRPC2Error;
import com.thetransactioncompany.jsonrpc2.JSONRPC2ParamsType;
import com.thetransactioncompany.jsonrpc2.JSONRPC2Response;

public class CreatePlumbingPort extends ApiHandler<Map<String, Object>> {
	
	@Override
	public JSONRPC2Response process(final Map<String, Object> params) {
		JSONRPC2Response resp = null;
		
		try {
			final Long physicalDpid = HandlerUtils.<Number> fetchField(
					TenantHandler.PHYSICAL_DPID, params, true, null).longValue();
			final Integer plumbingSwitchId = HandlerUtils.<Number> fetchField(
					TenantHandler.PLUMBING_SWITCH_ID, params, true, null).intValue();
			final Short physicalPort = HandlerUtils.<Number> fetchField(
					TenantHandler.PHYSICAL_PORT, params, true, null).shortValue();
			
			final PhysicalNetwork physicalNetwork = PhysicalNetwork.getInstance();
			final PhysicalSwitch physicalSwitch = physicalNetwork.getSwitch(physicalDpid);
			if (physicalPort == (short)0) {
				physicalSwitch.getPlumbingGraph().addPort(plumbingSwitchId, null);
			} else {
				physicalSwitch.getPlumbingGraph().addPort(plumbingSwitchId, physicalPort);
			}
			
		} catch (final MissingRequiredField e) {
	            resp = new JSONRPC2Response(new JSONRPC2Error(
	                    JSONRPC2Error.INVALID_PARAMS.getCode(), this.cmdName()
	                            + e.getMessage()), 0);
	    }
		
		resp = new JSONRPC2Response(0);
		return resp;
	}
	
	@Override
	public JSONRPC2ParamsType getType() {
		return JSONRPC2ParamsType.OBJECT;
	}
}
