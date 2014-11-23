package edu.princeton.cs.hsa;

import junit.framework.TestCase;
import junit.framework.TestSuite;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.openflow.protocol.OFFlowMod;

public class HsaTest extends TestCase {
	
	private static Logger log = LogManager.getLogger(HsaTest.class.getName());

    public HsaTest(final String name) {
        super(name);
    }

    /**
     * @return the suite of tests being tested
     */
    public static TestSuite suite() {
        return new TestSuite(HsaTest.class);
    }

    /*public void test1() {
    	
    	// build graph
    	PlumbingGraph graph = new PlumbingGraph();
    	graph.addNode((long) 1);
    	graph.addNode((long) 2);
    	graph.addNode((long) 3);
    	graph.addPort((long) 1, (short) 1, (short) 4);
    	graph.addPort((long) 1, (short) 2, null);
    	graph.addPort((long) 1, (short) 3, null);
    	graph.addPort((long) 2, (short) 1, null);
    	graph.addPort((long) 2, (short) 2, (short) 5);
    	graph.addPort((long) 2, (short) 3, null);
    	graph.addPort((long) 3, (short) 1, null);
    	graph.addPort((long) 3, (short) 2, null);
    	graph.addPort((long) 3, (short) 3, (short) 6);
    	graph.addEdge((long) 1, (short) 2, (long) 2, (short) 1);
    	graph.addEdge((long) 1, (short) 3, (long) 3, (short) 1);
    	graph.addEdge((long) 2, (short) 3, (long) 3, (short) 2);
    	
    	graph.update(RuleGenerationUtil.generateDefaultRule(), graph.getNode((long) 1));
    	graph.update(RuleGenerationUtil.generateDefaultRule(), graph.getNode((long) 2));
    	graph.update(RuleGenerationUtil.generateDefaultRule(), graph.getNode((long) 3));
    	
    	graph.update(RuleGenerationUtil.generatePrefixRoutingRule(1, "1.0.0.0", 8, 1, OFFlowMod.OFPFC_ADD), graph.getNode((long) 1));
    	graph.update(RuleGenerationUtil.generatePrefixRoutingRule(2, "2.2.2.0", 24, 3, OFFlowMod.OFPFC_ADD), graph.getNode((long) 1));
    	graph.update(RuleGenerationUtil.generatePrefixRoutingRule(1, "2.0.0.0", 8, 2, OFFlowMod.OFPFC_ADD), graph.getNode((long) 1));
    	graph.update(RuleGenerationUtil.generatePrefixRoutingRule(1, "3.0.0.0", 8, 3, OFFlowMod.OFPFC_ADD), graph.getNode((long) 1));
    	
    	graph.update(RuleGenerationUtil.generatePrefixRoutingRule(1, "1.0.0.0", 8, 1, OFFlowMod.OFPFC_ADD), graph.getNode((long) 2));
    	graph.update(RuleGenerationUtil.generatePrefixRoutingRule(1, "2.0.0.0", 8, 2, OFFlowMod.OFPFC_ADD), graph.getNode((long) 2));
    	graph.update(RuleGenerationUtil.generatePrefixRoutingRule(1, "3.0.0.0", 8, 3, OFFlowMod.OFPFC_ADD), graph.getNode((long) 2));
    	
    	graph.update(RuleGenerationUtil.generatePrefixRoutingRule(1, "1.0.0.0", 8, 1, OFFlowMod.OFPFC_ADD), graph.getNode((long) 3));
    	graph.update(RuleGenerationUtil.generatePrefixRoutingRule(1, "2.0.0.0", 8, 2, OFFlowMod.OFPFC_ADD), graph.getNode((long) 3));
    	graph.update(RuleGenerationUtil.generatePrefixRoutingRule(1, "3.0.0.0", 8, 3, OFFlowMod.OFPFC_ADD), graph.getNode((long) 3));
    	graph.update(RuleGenerationUtil.generatePrefixRoutingRule(2, "1.1.1.0", 24, 2, OFFlowMod.OFPFC_ADD), graph.getNode((long) 3));
    	
    	log.error(graph);
    	
    }*/
    
    @Override
    protected void setUp() throws Exception {
        super.setUp();
    }

    @Override
    protected void tearDown() throws Exception {
        super.tearDown();
    }
}
