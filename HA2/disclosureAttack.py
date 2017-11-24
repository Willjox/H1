#!/usr/bin/env python

from pcapfile import savefile
import ipaddress

testcap = open('cia.log.1337.pcap', 'rb')
capfile = savefile.load_savefile(testcap, layers=2, verbose=True)
nasir = input("Nasir adress: ")
mixer = input("mix address: " )

msgSet = set()
sets = []
prev = "0.0.0.0"
append = 0
r = []

def finddisjoint():
	disjoint = []
	for ry in sets:
		for rx in sets:
			if ry.isdisjoint(rx):

				disjoint.append(ry)
				disjoint.append(rx)
				return disjoint
def exclude():
	for rx in sets:
		if not r[0].isdisjoint(rx) and r[1].isdisjoint(rx):
			r[0] = r[0].intersection(rx)
		elif  r[0].isdisjoint(rx) and not r[1].isdisjoint(rx):
			r[1] = r[1].intersection(rx)
	result = r[0].union(r[1])
	return result





for pkt in capfile.packets:
	timestamp = pkt.timestamp
	ip_src = pkt.packet.payload.src.decode('UTF8')
	ip_dst = pkt.packet.payload.dst.decode('UTF8')

	if ip_src == nasir:
		append = 1
	if ip_src == mixer and append == 1:
		msgSet.add(ip_dst)


	if ip_src != mixer and prev == mixer and append == 1:
		append = 0
		if len(msgSet) > 0:
			sets.append(set(msgSet))
		msgSet = set()
	prev = ip_src

r = finddisjoint()
result = exclude()
ipint1 = int.from_bytes(ipaddress.IPv4Address(result.pop()).packed, byteorder='big', signed=False)
ipint2 = int.from_bytes(ipaddress.IPv4Address(result.pop()).packed, byteorder='big', signed=False)
print(ipint1+ipint2)
