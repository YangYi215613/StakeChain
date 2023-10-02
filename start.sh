#!/bin/bash

python main.py localhost 10001 5000 keys/genesisPrivateKey.pem &
python main.py localhost 10002 5001 keys/stakerPrivateKey.pem &

num=18
for ((i=0; i<$num; i++))
do
  port1=$((10003 + i))
  port2=$((5002 + i))
  python main.py localhost $port1 $port2 &
done

wait