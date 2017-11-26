#!/usr/bin/env python

from pcapfile import savefile
import ipaddress

testcap = open('cia.log.1339.pcap', 'rb')
capfile = savefile.load_savefile(testcap, layers=2, verbose=True)

nasir = "161.53.13.37" #input("Nasir adress: ")
mixer = "11.192.206.171" #input("Mix address: " )
partners = int(input("Number of partners: " ))


def disjoint(testList,testSet):
	for rx in testList:
		if not testSet.isdisjoint(rx):
			return False
	return True
def finddisjoint():
	rdis = []
	print(len(sets))

	for rx in sets:
		if disjoint(rdis,rx):
			rdis.append(rx)
			sets.remove(rx)
		elif rdis == partners:
			break
	print(len(sets))
	return rdis
def parse():
	append = 0
	msgSet = set()
	prev = "0.0.0.0"
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
def exclude():
	for rx in sets:
		for ri in r:
			if not rx.isdisjoint(ri):
				testList = list(r)
				testList.remove(ri)
				if disjoint(testList,rx):
					r.remove(ri)
					r.append(ri.intersection(rx))
	return
def unionize():
	union = set()
	for rx in r:
		union = union.union(rx)
	return union
def addIP(finalSet):
	ipint = 0
	while len(finalSet) !=0:
		v = int.from_bytes(ipaddress.IPv4Address(finalSet.pop()).packed, byteorder='big', signed=False)
		print(v)
		ipint = ipint + v
	print(ipint)
	return ipint

sets = []
parse()
r = finddisjoint()
exclude()
print(addIP(unionize()))
