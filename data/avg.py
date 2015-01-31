import sys
import glob, os

rootdir = sys.argv[1]
hostNum = sys.argv[2]

for i in range(1, int(hostNum)/10 + 1):
	hostdir = rootdir + '/' + str(i*10) + 'hosts'
	allfiles = glob.glob(hostdir + '/*')
	sum = 0
	counter = 0
	for file in allfiles:
		f = open(file)
		lines = f.readlines()
		f.close()
		for line in lines:
			sum = sum + int(line.split(',')[0])
			counter = counter + 1
	
	avg = float(sum) / counter

	print avg
	
		
