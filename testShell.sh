#!/bin/sh
time=$(date "+%Y-%m-%d %H：%M：%S")
echo "$time" >> ~/Desktop/time.txt

cd /Users/g/Documents/GitHub/python/Algorithmic-Trading-Tutorial

python "Tutorial 04 CN - Get intraday.py"




