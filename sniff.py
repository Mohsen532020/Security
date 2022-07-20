from scapy.all import *
def packet(p):
     print p.summary()
     print
     return
while True:
     sniff(iface="ens33",prn=packet)
	 
