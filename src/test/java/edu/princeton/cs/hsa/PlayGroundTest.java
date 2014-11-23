package edu.princeton.cs.hsa;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

import junit.framework.TestCase;
import junit.framework.TestSuite;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.openflow.protocol.OFFlowMod;

import edu.princeton.cs.policy.adv.PolicyACL;
import edu.princeton.cs.policy.adv.PolicyFlowTable;
import edu.princeton.cs.policy.adv.PolicyParseUtil;
import edu.princeton.cs.policy.adv.PolicyTree;
import edu.princeton.cs.policy.store.PolicyFlowModStore.PolicyFlowModStoreKey;
import edu.princeton.cs.policy.store.PolicyFlowModStore.PolicyFlowModStoreType;

public class PlayGroundTest extends TestCase {
	
	private static Logger log = LogManager.getLogger(PlayGroundTest.class.getName());

    public PlayGroundTest(final String name) {
        super(name);
    }

    /**
     * @return the suite of tests being tested
     */
    public static TestSuite suite() {
        return new TestSuite(PlayGroundTest.class);
    }

    public void test1() {
    	
    	/*List<Integer> x = new ArrayList<Integer>();
    	x.add(null);
    	x.add(1);
    	
    	if(x.get(0) == null) {
    		log.error("null");
    	}
    	
    	if(x.get(1) != null) {
    		log.error("not null");
    	}*/
    	
    	PolicyTree leftChild = new PolicyTree('1');
    	leftChild.tenantId = 1;
    	leftChild.policyACL = PolicyParseUtil.parseAclString("dltype:exact,srcip:prefix,dstip:prefix", "mod:dstip");
    	PolicyTree rightChild = new PolicyTree('2');
    	rightChild.tenantId = 2;
    	rightChild.policyACL = PolicyParseUtil.parseAclString("dltype:exact,dstip:prefix", "output");
    	PolicyTree root = new PolicyTree('>');
    	root.leftChild = leftChild;
		root.rightChild = rightChild;
		
		

		List<PolicyFlowModStoreType> storeTypes = new ArrayList<PolicyFlowModStoreType>();
		storeTypes.add(PolicyFlowModStoreType.EXACT);
		storeTypes.add(PolicyFlowModStoreType.PREFIX);
		storeTypes.add(PolicyFlowModStoreType.WILDCARD);
		List<PolicyFlowModStoreKey> storeKeys = new ArrayList<PolicyFlowModStoreKey>();
		storeKeys.add(PolicyFlowModStoreKey.DL_TYPE);
		storeKeys.add(PolicyFlowModStoreKey.NW_DST);
		storeKeys.add(PolicyFlowModStoreKey.ALL);
		
		leftChild.flowTable = new PolicyFlowTable(storeTypes, storeKeys, true);
		rightChild.flowTable = new PolicyFlowTable(storeTypes, storeKeys, false);
		root.flowTable = new PolicyFlowTable();
		
		
		System.out.println(root);
		
		root.update(OFFlowModHelper.genFlowMod("priority=0"), 1);
		root.update(OFFlowModHelper
				.genFlowMod("priority=3,ether-type=2048,src-ip=0.0.0.0/2,dst-ip=3.0.0.0,actions=set-dst-ip:2.0.0.1"), 1);
		root.update(OFFlowModHelper
				.genFlowMod("priority=1,ether-type=2048,dst-ip=3.0.0.0,actions=set-dst-ip:2.0.0.2"), 1);
		
		root.update(OFFlowModHelper.genFlowMod("priority=0"), 2);
		root.update(OFFlowModHelper.genFlowMod("priority=1,ether-type=2048,dst-ip=2.0.0.1,actions=output:1"), 2);
		root.update(OFFlowModHelper.genFlowMod("priority=1,ether-type=2048,dst-ip=2.0.0.2,actions=output:2"), 2);
		
		System.out.println(leftChild.flowTable);
		System.out.println(rightChild.flowTable);
		System.out.println(root.flowTable);
		
    	
    }
    
    
    
    @Override
    protected void setUp() throws Exception {
        super.setUp();
    }

    @Override
    protected void tearDown() throws Exception {
        super.tearDown();
    }
}
