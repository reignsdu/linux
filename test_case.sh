#!/bin/bash
#测试时间
hour='date+%H'
case $hour in
0[1-9]|1[01])
	echo "good morning!"
	;;
1[2-7])
	echo "good afternoon!"
	;;
*)
	echo "good evening!"
	;;
esac
