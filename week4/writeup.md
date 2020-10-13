Configure default route to the routers:

Procedure:

Three routers are placed on the same level and connected using serial DCE cable. The three routers are named as router0, router1 and router2.
A switch called switch0 is placed alongside router0 and another called switch1 is placed alongside router2. The connection between routers and switches is done using copper staright-through cables.
Two generic computers are placed alongside each switch. For switch0 the computers are named PC0 and PC1. For switch1 computers are named PC2 and PC3.
IP addresses and default gateway addresses are configured seperately for all four computers.
The terminal of each router is accessed and the interfaces for each connection is established with specified gateway addresses.

Observations:

Pinging any destination computer from any source initially gives an error stating destination host unreachable because there is no direct connection between source and destination.
The ip route of the routers can be seen using show ip route command for each router.
In order to send ping message irrespective of destination addresses via routers we add default routes to routers router0 and router2.This can be done as follows:

For router0:
Route through 10.0.0.0 and 20.0.0.0 is directly connected. Therefore, we add default route with next hop address as 20.0.0.2.
Router(config)#ip route 0.0.0.0 0.0.0.0 20.0.0.2
For router2:
Route through 30.0.0.0 and 40.0.0.0 is directly connected. Therefore, we add default route with next hop address as 30.0.0.1.
Router(config)#ip route 0.0.0.0 0.0.0.0 30.0.0.1

For router1:
Route through 20.0.0.0 and 30.0.0.0 is directly connected. Therefore, we add static route through 10.0.0.0 and 40.0.0.0.
Router(config)#ip route 10.0.0.0 255.0.0.0 20.0.0.1
Router(config)#ip route 40.0.0.0 255.0.0.0 30.0.0.2
After adding default routes to routers, router0 and router2, a connection is established between each interface and pinging from any source to any destination works as per the requirement.

Learning Outcomes:

Configuring a topology with multiple routers.
Configuring IP and default gateway addresses for PCs.
Configuring IP addresses for interfaces.
Configuring static IP routes for ping messages to give the desired response since they give an error if there is no direct connection between device networks.
Configuring default IP routes to routers such that irrespective of destination address the packet is forwarded to the next hop address specified.