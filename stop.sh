#!/bin/bash

# warning: 注意其它无关进行是否也执行python main.py，如果有，需要进行命令修改
pids=$(pgrep -f "python main.py")

for pid in $pids
do
  kill $pid
done