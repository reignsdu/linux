#!/bin/bash
#打印数组最小值
smallest=10000
for i in 12 5 18 58 -3 80
do
if test $i -lt $smallest
then
	smallest=$i
fi
done
echo " the smallest number is: $smallest"
