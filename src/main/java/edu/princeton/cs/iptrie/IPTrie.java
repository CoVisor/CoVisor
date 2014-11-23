package edu.princeton.cs.iptrie;

import java.util.ArrayList;
import java.util.List;

public class IPTrie<O> {
	
	public class TrieNode {
		public O value;
		public List<TrieNode> children;
		
		public TrieNode(O value) {
			this.value = value;
			this.children = new ArrayList<TrieNode>();
			this.children.add(null);
			this.children.add(null);
		}
	}
	
	private TrieNode root;
	
	public IPTrie() {
		this.root = new TrieNode(null);
	}
	
	public void put (String key, O value) {
		TrieNode curNode = root;
		TrieNode nextNode = null;
		for (int i = 0; i < key.length(); i++) {
			
			if (key.charAt(i) == '0') {
				
				nextNode = curNode.children.get(0);
				if (nextNode == null) {
					nextNode = new TrieNode(null);
					curNode.children.set(0, nextNode);
				}
				
			} else {
				
				nextNode = curNode.children.get(1);
				if (nextNode == null) {
					nextNode = new TrieNode(null);
					curNode.children.set(1, nextNode);
				}
				
			}
			
			curNode = nextNode;
		}
		curNode.value = value;
	}
	
	public List<O> get (String key) {
		List<O> res = new ArrayList<O>();
		
		TrieNode curNode = root;
		TrieNode nextNode = null;
		for (int i = 0; i < key.length(); i++) {
			if (key.charAt(i) == '0') {
				nextNode = curNode.children.get(0);
			} else {
				nextNode = curNode.children.get(1);
			}
			
			if (nextNode == null) {
				return res;
			}
			curNode = nextNode;
			if(curNode.value != null) {
				res.add(curNode.value);
			}
		}
		
		this.DFS(res, curNode.children.get(0));
		this.DFS(res, curNode.children.get(1));
		
		return res;
	}
	
	private void DFS(List<O> res, TrieNode curNode) {
		if (curNode == null) {
			return;
		}
		
		if (curNode.value != null) {
			res.add(curNode.value);
		}
		DFS(res, curNode.children.get(0));
		DFS(res, curNode.children.get(1));
	}
	
	public O getExact (String key) {
		TrieNode curNode = root;
		TrieNode nextNode = null;
		for (int i = 0; i < key.length(); i++) {
			if (key.charAt(i) == '0') {
				nextNode = curNode.children.get(0);
			} else {
				nextNode = curNode.children.get(1);
			}
			
			if (nextNode == null) {
				return null;
			}
			curNode = nextNode;
		}
		return curNode.value;
	}

}
