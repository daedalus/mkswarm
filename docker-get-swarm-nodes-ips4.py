#!/usr/bin/env python
# Author Dario Clavijo 2019
# GPLv3

import docker
import sys
import random

new_manager = sys.argv[2]
token = sys.argv[3]
token_m = sys.argv[4]
rate = int(sys.argv[5])

def reconnect_node(ip,manager,token):
    print "torify docker -H %s swarm leave --force" % ip
    print "torify docker -H %s swarm join --token %s %s:2377" % (ip,token,manager)

def promote_node(manager,node):
    print "torify docker -H %s node promote %s" % (manager,node)
    #print

print "#!/bin/bash"
print "set -x"

n=0
nodes = []

fp = open(sys.argv[1])
for line in fp:
	nodes.append(line.rstrip())
random.shuffle(nodes)
for node in nodes:
        ip = node
        c = True
        if c:
            if ip != new_manager:
                if n % rate ==0:
			reconnect_node(ip,new_manager,token_m)
		else:
                	reconnect_node(ip,new_manager,token)
	n+=1
