package edu.princeton.cs.policy.adv;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Stack;

import org.apache.commons.lang.NotImplementedException;

import net.onrc.openvirtex.exceptions.NetworkMappingException;
import edu.princeton.cs.policy.adv.PolicyTree.PolicyOperator;
import edu.princeton.cs.policy.store.PolicyFlowModStore.PolicyFlowModAction;
import edu.princeton.cs.policy.store.PolicyFlowModStore.PolicyFlowModStoreKey;
import edu.princeton.cs.policy.store.PolicyFlowModStore.PolicyFlowModStoreType;

public class PolicyParseUtil {
	
	/*
	 * Example:
	 * aclMatch: srcip:exact,dstip:exact
	 * aclAction: output,mod:dstip
	 */
	public static PolicyACL parseAclString(String aclMatch, String aclAction) {
		
		PolicyACL policyACL = new PolicyACL();
		
		// parse aclMatch
		for (String fieldType : aclMatch.split(",")) {
			String[] temp = fieldType.split(":");
			PolicyFlowModStoreKey field = parseAclField(temp[0]);
			PolicyFlowModStoreType type = parseAclType(temp[1]);
			policyACL.aclMatch.put(field, type);
		}
		
		// parse aclAction
		for (String actionStr : aclAction.split(",")) {
			PolicyFlowModAction action = parseAclAction(actionStr);
			policyACL.aclAction.put(action, true);
		}

		return policyACL;
	}
	
	private static PolicyFlowModStoreKey parseAclField(String str) {
		switch (str) {
		case "input":
			return PolicyFlowModStoreKey.IN_PORT;
		case "vlan":
			return PolicyFlowModStoreKey.DL_VLAN;
		case "srcmac":
			return PolicyFlowModStoreKey.DL_SRC;
		case "dstmac":
			return PolicyFlowModStoreKey.DL_DST;
		case "dltype":
			return PolicyFlowModStoreKey.DL_TYPE;
		case "proto":
			return PolicyFlowModStoreKey.NW_PROTO;
		case "srcport":
			return PolicyFlowModStoreKey.TP_SRC;
		case "dstport":
			return PolicyFlowModStoreKey.TP_DST;
		case "srcip":
			return PolicyFlowModStoreKey.NW_SRC;
		case "dstip":
			return PolicyFlowModStoreKey.NW_DST;
		case "vlanpcp":
			return PolicyFlowModStoreKey.DL_VLAN_PCP;
		case "tos":
			return PolicyFlowModStoreKey.NW_TOS;
		default:
			throw new NotImplementedException("not implemented match field");
		}
	}
	
	private static PolicyFlowModStoreType parseAclType(String str) {
		switch (str){
		case "exact":
			return PolicyFlowModStoreType.EXACT;
		case "prefix":
			return PolicyFlowModStoreType.PREFIX;
		case "wildcard":
			return PolicyFlowModStoreType.WILDCARD;
		default:
			return PolicyFlowModStoreType.DISALLOW;
		}
	}
	
	private static PolicyFlowModAction parseAclAction(String str) {
		switch (str){
		case "mod:srcmac":
			return PolicyFlowModAction.DataLayerSource;
		case "mod:dstmac":
			return PolicyFlowModAction.DataLayerDestination;
		case "mod:srcip":
			return PolicyFlowModAction.NetworkLayerSource;
		case "mod:dstip":
			return PolicyFlowModAction.NetworkLayerDestination;
		case "output":
			return PolicyFlowModAction.Output;
		case "mod:srcport":
			return PolicyFlowModAction.TransportLayerSource;
		case "mod:dstport":
			return PolicyFlowModAction.TransportLayerDestination;
		default:
			throw new NotImplementedException("not implemented acl action");
		}
	}
	
	/*
	 * Example: 1 + 2/3 > 4
	 */
	public static PolicyTree parsePolicyString(String policy) throws NetworkMappingException {
        System.out.println("enter parse policy ----------------------------------------");
		List<PolicyTree> postfix = transformToPostfixForm(policy);
		PolicyTree policyTree = buildPolicyTree(postfix);
		policyTree.initializeFlowTable();
		policyTree.flowTable = new PolicyFlowTable();

		System.out.println(policyTree);
		
		return policyTree;
	}
	
	private static List<PolicyTree> transformToPostfixForm(String policy) {
		Stack<Character> stack = new Stack<Character>();
		List<PolicyTree> postfix = new ArrayList<PolicyTree>();
		Map<Integer, PolicyTree> tenantNodeMap = new HashMap<Integer, PolicyTree>();

		for (int i = 0; i < policy.length(); i++) {
			Character ch = policy.charAt(i);
			if (Character.isDigit(ch)) {
				
				int tenantId = ch - '0';
				while (i+1 < policy.length() && Character.isDigit(policy.charAt(i+1))) {
					i++;
					tenantId = tenantId * 10 + policy.charAt(i) - '0';
				}
				
				PolicyTree policyTree = tenantNodeMap.get(tenantId);
				if (policyTree == null) {
					policyTree = new PolicyTree();
					policyTree.tenantId = tenantId;
					tenantNodeMap.put(tenantId, policyTree);
				}
						
				postfix.add(policyTree);
				
			} else if (ch == '(') {
				stack.push(ch);
			} else if (ch == ')') {
				while (stack.peek() != '(') {
					postfix.add(new PolicyTree(stack.pop()));
				}
				stack.pop();
			} else {
				while (!stack.isEmpty() && compareOperatorPriority(stack.peek(), ch)) {
					postfix.add(new PolicyTree(stack.pop()));
				}
				stack.push(ch);
			}
		}
		while (!stack.isEmpty()) {
			postfix.add(new PolicyTree(stack.pop()));
		}
		
		return postfix;
	}
	
	private static boolean compareOperatorPriority(char peek, char cur) {
		if (peek == '/' && (cur == '+' || cur == '>' || cur == '/')) {
			return true;
		} else if (peek == '>' && (cur == '+' || cur == '>')) {
			return true;
		} else if (peek == '+' && cur == '+') {
			return true;
		}
		return false;
	}
	
	private static PolicyTree buildPolicyTree(List<PolicyTree> postfix) {
		Stack<PolicyTree> stack = new Stack<PolicyTree>();
		for (PolicyTree node : postfix) {
			if(node.operator == PolicyOperator.Tenant) {
				stack.push(node);
			} else {
				node.rightChild = stack.pop();
				node.leftChild = stack.pop();
				stack.push(node);
			}
		}
		return stack.pop();
	}

}
