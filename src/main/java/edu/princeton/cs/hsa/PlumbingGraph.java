package edu.princeton.cs.hsa;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

import net.onrc.openvirtex.elements.datapath.PhysicalSwitch;
import net.onrc.openvirtex.messages.OVXFlowMod;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.openflow.protocol.OFFlowMod;

import edu.princeton.cs.policy.adv.PolicyFlowTable;
import edu.princeton.cs.policy.adv.PolicyUpdateTable;
import edu.princeton.cs.policy.store.PolicyFlowModStore.PolicyFlowModStoreKey;
import edu.princeton.cs.policy.store.PolicyFlowModStore.PolicyFlowModStoreType;

public class PlumbingGraph {
	
    public static final int PRIORITY_HOPS = 3;
	
    private Logger logger = LogManager.getLogger(PlumbingGraph.class.getName());
    
    private PhysicalSwitch physicalSwitch;
    private Map<Integer, PlumbingSwitch> nodes;
    public PolicyFlowTable flowTable;
    
    public PlumbingGraph(PhysicalSwitch physicalSwitch) {
	this.physicalSwitch = physicalSwitch;
	this.nodes = new HashMap<Integer, PlumbingSwitch>();
	this.flowTable = new PolicyFlowTable();
    }
    
    public PhysicalSwitch getPhysicalSwitch() {
	return this.physicalSwitch;
    }
    
    public void createNodes (int count) {
	for (int i = 0; i < count; i++) {
	    PlumbingSwitch node = new PlumbingSwitch(i, this);
	    this.nodes.put(i, node);
	}
    }
    
    public void addNode (int id) {
	PlumbingSwitch node = new PlumbingSwitch(id, this);
	this.nodes.put(id, node);
    }
    
    public void addPort(int id, Short physicalPort) {
		this.nodes.get(id).addPort(physicalPort);
    }
    
    public void addEdge(int id1, short port1, int id2, short port2) {
	PlumbingSwitch node1 = this.nodes.get(id1);
	PlumbingSwitch node2 = this.nodes.get(id2);
	
	node1.addNextHop(port1, node2, port2);
	node2.addNextHop(port2, node1, port1);
    }
    
    public PlumbingSwitch getNode(int id) {
	return this.nodes.get(id);
    }
    
    public PolicyUpdateTable update(OVXFlowMod ofm, PlumbingSwitch node) {
        if (this.nodes.size() == 1) {
            return this.flowTable.update(ofm);
        } else {
	    PolicyUpdateTable updateTable = node.update(ofm);
	    for (OVXFlowMod fm : updateTable.addFlowMods) {
		this.flowTable.addFlowMod(fm);
	    }
	    return updateTable;
        }
    }
    
    public String getGraphString() {
	String str = "";
	for (PlumbingSwitch node : this.nodes.values()) {
	    str = str + node.toString();
	}
	return str;
    }
    
    @Override
    public String toString() {
	String str = "Flow Table:\n";
	for (OFFlowMod fm : this.flowTable.getFlowModsSortByInport()) {
	    str = str + fm.toString() + "\n";
	}
	
	/*for (PlumbingNode node : this.nodes.values()) {
	  str = str + node.dpid + "\n" + node.getFlowModString();
	  }*/
	return str;
    }
    
}
