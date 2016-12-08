#!/bin/bash
#c测试当前用户是否为user
	echo -n "Enter your login name:"
	read name
	if [ "$name" = "$USER" ];
	then
		echo "Hello,$name.how are you today ?"
	else
		echo "You are not $USER ,so who are yo ?"
	fi
