#!/bin/bash
#比较s1和s2是否相同
echo "please input string1:"
read -r s1
echo "please input string2:"
read -r s2
if [ "$s1" = "$s2" ]
	then
	 echo "string1 is equal to string2"
	else
	 echo "string1 is not equal to string2"
fi
