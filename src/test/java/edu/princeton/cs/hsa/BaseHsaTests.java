package edu.princeton.cs.hsa;

import junit.framework.Test;
import junit.framework.TestSuite;

public final class BaseHsaTests {
	
	private BaseHsaTests() {
    }

    public static Test suite() {
        final TestSuite suite = new TestSuite(BaseHsaTests.class.getName());
        // $JUnit-BEGIN$
        suite.addTest(PlayGroundTest.suite());
        // $JUnit-END$
        return suite;
    }

}
