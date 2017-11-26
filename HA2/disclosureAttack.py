#!/usr/bin/env python

from pcapfile import savefile
import ipaddress

testcap = open('cia.log.1337.pcap', 'rb')
capfile = savefile.load_savefile(testcap, layers=2, verbose=True)

nasir = "159.237.13.37" #input("Nasir adress: ")
mixer = "94.147.150.188" #input("Mix address: " )
partners = int(input("Number of partners: " ))

msgSet = set()
sets = []
prev = "0.0.0.0"
append = 0
r = []

def finddisjoint():
	for rx in sets:
		outputList=list()
		outputList.append(rx)
		for ry in sets:
			appendOutput = 0
			for rz in outputList:
				if not rz.isdisjoint(ry):
					appendOutput = -1
			if appendOutput == 0:
				print("Appending ry")
				outputList.append(ry)

			if (len(outputList) == partners):
				print("Before returning outputlist")
				return outputList
	return list()


def exclude():
	output = list()
	for rx in r:
		for ry in sets:
			if not rx.isdisjoint(ry):
				rx = rx.intersection(ry)
				if len(rx) == 1:
					output.append(rx)
				#addtoout = 0
				#for rz in r:
				#	if not ry.isdisjoint(rz):
				#		addtoout+= 1
				#if addtoout == 1:
				#	print(rx)
				#	rx = ry.intersection(rx)
	print(output)
	R = set()
	for xy in output:
		R = R.union(xy)
	print(R)
	output = list()
	output.append(R)
	return R

def addIP(finalSet):
	ipint = 0
	while len(finalSet) !=0:
		v = int.from_bytes(ipaddress.IPv4Address(finalSet.pop()).packed, byteorder='big', signed=False)
		print(v)
		ipint = ipint + v
	print(ipint)	
	return ipint


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
#print(r)
finalSet = exclude()
#print(r)
print(addIP(finalSet))
