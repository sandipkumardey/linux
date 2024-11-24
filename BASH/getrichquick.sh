#!/bin/bash

name=$1
age=$2

echo "Hello $1, you are $2 years old!!"

sleep 2

echo "Calculating"
echo "..........."
sleep 1
echo "**........."
sleep 1
echo "****......."
sleep 1
echo "******....."
sleep 1
echo "***********"



getrich=$((( $RANDOM % 15 )+ $2 ))

echo "$1, you will become a billionare when you are $getrich years old"
