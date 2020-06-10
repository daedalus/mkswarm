#!/bin/bash
# Author Dario Clavijo 2019
# GPLv3 

set -x

# call
#  mkswarm <file_ips> <ip_manager> <manager_rate> <output_script> 

MANAGER=$2


torify docker -H $MANAGER swarm leave --force
torify docker -H $MANAGER swarm init

export WTK=$(torify docker -H $MANAGER swarm join-token worker | grep -e '--token' | awk  '{ print $5 }')
export MTK=$(torify docker -H $MANAGER swarm join-token manager | grep -e '--token' | awk '{ print $5 }')
python code/misc/docker-get-swarm-nodes-ips4.py $1 $MANAGER $WTK $MTK $3 > $4; 
#scp nodes.sh 172.26.5.76:/tmp/
#bash nodes.sh
