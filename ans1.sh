#!/bin/bash
#输入A，B，比较A，B大小并由小值加到大值
sum=0
echo "please input A and B"
read A B
check()
{
if [ "$1" -gt "$2" ]
	then
	return 1
	else
	return 0
fi	
}

check $A $B
if [ $? -eq 0 ]
	then
	 echo "B is bigger"
	 while [ $A -le $B ]
	 do
		sum=`expr $sum + $A`
		A=`expr $A + 1`
	 done
	else
	 echo "A is bigger"
	 while [ $B -le $A ]
	 do
		sum=`expr $sum + $B`
		B=`expr $B + 1`
	 done
fi

echo "the sum is:"
echo $sum
