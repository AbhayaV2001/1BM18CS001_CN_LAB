<h1>Configure DHCP in a Local Area Network:</h1>

<h3>Procedure:</h3>
<ol>
<li>A router is placed namely router0.</li>
<li>A switch called switch0 is placed alongside router0 and is connected to a server named server0.</li>
<li>Four generic computers are placed alongside the switch as well. For switch0 the computers are named PC0, PC1, PC2 and PC3.</li>
<li>The terminal of the router is accessed and the interface for the connection is established with specified gateway address.</li>
<li>The server is then configured as a DHCP server with gateway, DNS server and TFTP addresses being specified.</li>
</ol>
<h3>Observations</h3>:
<ol>
<li>The PCs request the DHCP server for an IP address. Upon request an IP address is successfully assigned to the PC dynamically by the DHCP server.</li>
<li>Pinging the addresss 127.0.0.0 sends the ping message to the same PC as the address is called loop-back address which addresses the same PC.</li>

<h3>Learning Outcomes:</h3>
<ol>
<li>Creating a topology with router, switch, server and PCs.</li>
<li>Configuring the server as a DHCP server.</li>
<li>4 steps in DHCP:</li>
<ul>
  <li>D - Discover the server</li>
  <li>O - Offer the IP address</li>
  <li>R - Request IP</li>
  <li>A - Acknowledgement</li></ul>

<li>Individual PC request the server for an IP address.</li>
<li>An IP address is assigned to the PC from a pool of IP addresses by the DHCP server.<li>
