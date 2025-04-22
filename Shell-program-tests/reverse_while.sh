#!/bin/bash
read -p "Enter number: " num
rev=0
while [ $num -ne 0 ]; do
  digit=$((num % 10))
  rev=$((rev * 10 + digit))
  num=$((num / 10))
done
echo "Reversed number: $rev"
