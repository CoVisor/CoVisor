package net.onrc.openvirtex.api.service.handlers.tenant;

import java.util.Map;

import net.onrc.openvirtex.api.service.handlers.ApiHandler;
import net.onrc.openvirtex.elements.datapath.PhysicalSwitch;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import com.thetransactioncompany.jsonrpc2.JSONRPC2ParamsType;
import com.thetransactioncompany.jsonrpc2.JSONRPC2Response;

public class StopComposition extends ApiHandler<Map<String, Object>> {

	private Logger log = LogManager.getLogger(StopComposition.class.getName());
	
	@Override
	public JSONRPC2Response process(final Map<String, Object> params) {
		PhysicalSwitch.IsCompositionOn = false;
		this.log.info("composition off");
		return new JSONRPC2Response(0);
	}

	@Override
	public JSONRPC2ParamsType getType() {
		return JSONRPC2ParamsType.OBJECT;
	}

}
