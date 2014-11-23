CoVisor
==========


CoVisor is a new kind of network hypervisor that enables, in a single
network, the deployment of multiple control applications written in different
programming languages and operating on different controller platforms.  Unlike
past hypervisors, which focused on slicing the network into disjoint
parts for separate control by separate entities, CoVisor allows multiple
controllers to cooperate on managing the same shared traffic.
Consequently, network administrators can use CoVisor to assemble a collection of
independently-developed ``best of breed" applications---a firewall, a load
balancer, a gateway, a router, a traffic monitor---and can apply those
applications in combination, or separately, to the desired traffic.  CoVisor
also abstracts concrete topologies, providing custom virtual topologies in their
place, and allows administrators to specify access controls that regulate the
packets a given controller may see, modify, monitor, or reroute.

