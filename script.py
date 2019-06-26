#!/bin/python

import os 


for t in [1, 2, 4, 8]:
	#print "Threads = %d" % t
	cmd = "/usr/local/common/gcc-7.3.0/bin/g++ -DNUMT=%d proj2.cpp -o proj2 -lm -fopenmp" % t
	os.system(cmd)
	cmd = "./proj2"
	os.system(cmd)
