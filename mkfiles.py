#!/usr/bin/python

import glob, sys
import commands, os
import shutil

exp_name = sys.argv[1]

hostlist = []

f = open('usablehosts', 'r')

for host in f:
	hostlist.append(host)

f.close()

for hostNum in range(1, 101):
	dir_name = "data/" + exp_name + "/" + str(hostNum*10) + "hosts"

	if os.path.exists(dir_name):
		shutil.rmtree(dir_name)
	os.makedirs(dir_name)
		
