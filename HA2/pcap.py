#!/usr/bin/env python

from pcapfile import savefile

testcap = open('cia.log.1337.pcap', 'rb')
capfile = savefile.load_savefile(testcap, layers=2, verbose=True)
nasir = "159.237.13.37"
mixer = "94.147.150.188"

array =[]
sets = []
prev = "0.0.0.0"
append = 0

# print the packets
print ('timestamp\teth src\t\t\teth dst\t\t\tIP src\t\tIP dst')
for pkt in capfile.packets:
	timestamp = pkt.timestamp
	ip_src = pkt.packet.payload.src.decode('UTF8')
	ip_dst = pkt.packet.payload.dst.decode('UTF8')
	if ip_src == nasir:
		append = 1
	if ip_src == mixer and append == 1:
		array.append(ip_dst)
	if ip_src != mixer and prev == mixer:
		append = 0
		save = 1
		array = set(array)
		for list in sets:
			if array == list:
				save = 0
		if save == 1:
			sets.append(set(array))
		array = []	
	prev = ip_src
print(sets)


