package edu.princeton.cs.hsa;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

import org.openflow.protocol.OFMatch;

public class PlumbingFlow {
	
	private OFMatch match;
	private PlumbingFlowMod prevPmod;
	private PlumbingFlowMod nextPmod;
	private PlumbingFlow prevPflow;
	private List<PlumbingFlow> nextPflow;
	
	
	public PlumbingFlow (OFMatch match, PlumbingFlowMod prevPmod,
			PlumbingFlowMod nextPmod, PlumbingFlow prevPflow) {
		this.match = match;
		this.prevPmod = prevPmod;
		if (prevPmod != null) {
			prevPmod.addNextPFlow(this);
		}
		this.nextPmod = nextPmod;
		if (nextPmod != null) {
			nextPmod.addPrevPFlow(this);
		}
		this.prevPflow = prevPflow;
		this.nextPflow = new ArrayList<PlumbingFlow>();
	}
	
	public OFMatch getMatch() {
		return this.match;
	}
	
	public PlumbingFlowMod getPrevPMod() {
		return this.prevPmod;
	}
	
	public PlumbingFlowMod getNextPMod() {
		return this.nextPmod;
	}
	
	public PlumbingFlow getPrevPFlow() {
		return this.prevPflow;
	}
	
	public Collection<PlumbingFlow> getNextPFlows() {
		return this.nextPflow;
	}
	
	public void addNextPFlow(PlumbingFlow pflow) {
		this.nextPflow.add(pflow);
	}
}
