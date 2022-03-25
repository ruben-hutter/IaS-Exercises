# Answers IaS-Exercise 2
### Tobias Hafner, Ruben Hutter

## Exercise 1
a) IP: 130.59.31.80

ADDRESS: CH-8021 Zürich

OWNER: SWITCH-LAN 

b)

|Address |Ping |Browser |Comment|
|---|---|---|---|
|informatik.unibas.ch|yes|yes||
|www.zurich.ibm.com|no|yes|The IBM-Server isn't pingable for security reasons as a ping can be used to test if a server exists and responds.|
|www.tik.ee.ethz.ch|yes|yes||
|www.amazon.com|yes|yes||

## Exercise 2
i)

||56 byte|112 byte|224 byte|
|---|---|---|---|
|min [ms]|8.204|9.646|17.084|
|average [ms]|8.246|9.120|10.290|
|max [ms]|8.176|10.992|29.849|

**Command and output for 56 byte ping:**
	
	ping web.mit.edu -c 10
	ING e9566.dscb.akamaiedge.net (23.37.44.254) 56(84) bytes of data.
	64 bytes from a23-37-44-254.deploy.static.akamaitechnologies.com (23.37.44.254):
	icmp_seq=1 ttl=59 time=9.10 ms
	64 bytes from a23-37-44-254.deploy.static.akamaitechnologies.com (23.37.44.254):
	icmp_seq=2 ttl=59 time=8.79 ms
	64 bytes from a23-37-44-254.deploy.static.akamaitechnologies.com (23.37.44.254):
	icmp_seq=3 ttl=59 time=8.63 ms
	64 bytes from a23-37-44-254.deploy.static.akamaitechnologies.com (23.37.44.254):
	icmp_seq=4 ttl=59 time=8.20 ms
	64 bytes from a23-37-44-254.deploy.static.akamaitechnologies.com (23.37.44.254):
	icmp_seq=5 ttl=59 time=8.26 ms
	64 bytes from a23-37-44-254.deploy.static.akamaitechnologies.com (23.37.44.254):
	icmp_seq=6 ttl=59 time=9.06 ms
	64 bytes from a23-37-44-254.deploy.static.akamaitechnologies.com (23.37.44.254):
	icmp_seq=7 ttl=59 time=9.09 ms
	64 bytes from a23-37-44-254.deploy.static.akamaitechnologies.com (23.37.44.254):
	icmp_seq=8 ttl=59 time=8.52 ms
	64 bytes from a23-37-44-254.deploy.static.akamaitechnologies.com (23.37.44.254):
	icmp_seq=9 ttl=59 time=9.74 ms
	64 bytes from a23-37-44-254.deploy.static.akamaitechnologies.com (23.37.44.254):
	icmp_seq=10 ttl=59 time=17.1 ms

	--- e9566.dscb.akamaiedge.net ping statistics ---
	10 packets transmitted, 10 received, 0% packet loss, time 9016ms
	rtt min/avg/max/mdev = 8.204/9.646/17.084/2.516 ms

**Command and output for 112 byte ping:**
	
	ping web.mit.edu -c 10 -s 112
	PING e9566.dscb.akamaiedge.net (23.37.44.254) 112(140) bytes of data.
	120 bytes from a23-37-44-254.deploy.static.akamaitechnologies.com (23.37.44.254):
	icmp_seq=1 ttl=59 time=10.1 ms
	120 bytes from a23-37-44-254.deploy.static.akamaitechnologies.com (23.37.44.254):
	icmp_seq=2 ttl=59 time=9.42 ms
	120 bytes from a23-37-44-254.deploy.static.akamaitechnologies.com (23.37.44.254):
	icmp_seq=3 ttl=59 time=9.80 ms
	120 bytes from a23-37-44-254.deploy.static.akamaitechnologies.com (23.37.44.254):
	icmp_seq=4 ttl=59 time=8.62 ms
	120 bytes from a23-37-44-254.deploy.static.akamaitechnologies.com (23.37.44.254):
	icmp_seq=5 ttl=59 time=10.3 ms
	120 bytes from a23-37-44-254.deploy.static.akamaitechnologies.com (23.37.44.254):
	icmp_seq=6 ttl=59 time=8.25 ms
	120 bytes from a23-37-44-254.deploy.static.akamaitechnologies.com (23.37.44.254):
	icmp_seq=7 ttl=59 time=8.50 ms
	120 bytes from a23-37-44-254.deploy.static.akamaitechnologies.com (23.37.44.254):
	icmp_seq=8 ttl=59 time=9.03 ms
	120 bytes from a23-37-44-254.deploy.static.akamaitechnologies.com (23.37.44.254):
	icmp_seq=9 ttl=59 time=8.70 ms
	120 bytes from a23-37-44-254.deploy.static.akamaitechnologies.com (23.37.44.254):
	icmp_seq=10 ttl=59 time=8.54 ms

	--- e9566.dscb.akamaiedge.net ping statistics ---
	10 packets transmitted, 10 received, 0% packet loss, time 9015ms
	rtt min/avg/max/mdev = 8.246/9.120/10.290/0.685 ms

**Command and output for 224 byte ping:**
	
	ping web.mit.edu -c 10 -s 224
	PING e9566.dscb.akamaiedge.net (23.37.44.254) 224(252) bytes of data.
	232 bytes from a23-37-44-254.deploy.static.akamaitechnologies.com (23.37.44.254):
	icmp_seq=1 ttl=59 time=29.8 ms
	232 bytes from a23-37-44-254.deploy.static.akamaitechnologies.com (23.37.44.254):
	icmp_seq=2 ttl=59 time=8.69 ms
	232 bytes from a23-37-44-254.deploy.static.akamaitechnologies.com (23.37.44.254):
	icmp_seq=3 ttl=59 time=8.44 ms
	232 bytes from a23-37-44-254.deploy.static.akamaitechnologies.com (23.37.44.254):
	icmp_seq=4 ttl=59 time=8.53 ms
	232 bytes from a23-37-44-254.deploy.static.akamaitechnologies.com (23.37.44.254):
	icmp_seq=5 ttl=59 time=8.99 ms
	232 bytes from a23-37-44-254.deploy.static.akamaitechnologies.com (23.37.44.254):
	icmp_seq=6 ttl=59 time=8.67 ms
	232 bytes from a23-37-44-254.deploy.static.akamaitechnologies.com (23.37.44.254):
	icmp_seq=7 ttl=59 time=9.26 ms
	232 bytes from a23-37-44-254.deploy.static.akamaitechnologies.com (23.37.44.254):
	icmp_seq=8 ttl=59 time=9.02 ms
	232 bytes from a23-37-44-254.deploy.static.akamaitechnologies.com (23.37.44.254):
	icmp_seq=9 ttl=59 time=10.3 ms
	232 bytes from a23-37-44-254.deploy.static.akamaitechnologies.com (23.37.44.254):
	icmp_seq=10 ttl=59 time=8.18 ms

	--- e9566.dscb.akamaiedge.net ping statistics ---
	10 packets transmitted, 10 received, 0% packet loss, time 9013ms
	rtt min/avg/max/mdev = 8.176/10.992/29.845/6.309 ms

**Conclusion:**
The packagesize doesn't seem to have a significant effect on the Round-Trip-Time.

ii)
As "Sheldon's Office" is at CALTEC we use traceroute to find that there are 11 hops from unibas to www.caltec.edu.

**Command and output:**

	ruben@debian:~$ traceroute www.caltech.edu
	traceroute to www.caltech.edu (104.18.14.60), 30 hops max, 60 byte packets
	 1  _gateway (192.168.122.1)  0.405 ms  0.337 ms  0.311 ms
	 2  10.172.255.254 (10.172.255.254)  5.635 ms  5.606 ms  5.584 ms
	 3  10.36.253.6 (10.36.253.6)  5.560 ms  5.540 ms  5.505 ms
	 4  * * *
	 5  192.43.192.196 (192.43.192.196)  7.118 ms  7.096 ms  7.021 ms
	 6  swiBS1-100GE-0-0-0-0.switch.ch (130.59.37.34)  8.176 ms  4.013 ms  3.927 ms
	 7  swiPS1-100GE-0-0-1-3.switch.ch (130.59.37.190)  5.530 ms  4.536 ms  4.418 ms
	 8  swiPS2-100GE-0-0-1-4.switch.ch (130.59.37.58)  4.374 ms  4.727 ms  4.682 ms
	 9  swiZH3-100GE-0-0-0-2.switch.ch (130.59.36.170)  5.302 ms  5.237 ms  5.194 ms
	10  as13335.swissix.ch (91.206.52.192)  6.055 ms  6.529 ms  6.378 ms
	11  104.18.14.60 (104.18.14.60)  5.724 ms  6.185 ms  5.262 ms

iii)
Los Angeles - CA - US
Los Angeles - CA - US
Los Angeles - CA - US
Amsterdam - NL
Basel, Switzerland - CH
Zurich, Switzerland - CH
Zurich, Switzerland - CH
Zurich, Switzerland - CH
Zurich, Switzerland - CH
San Francisco - CA - US

The signal travels through the United States, the Netherlands and Switzerland.

iv)
