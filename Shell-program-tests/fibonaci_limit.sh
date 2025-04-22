#!/bin/bash
read -p "Enter limit: " limit
a=0
b=1

while [ $a -le $limit ]; do
  echo -n "$a "
  fn=$((a + b))
  a=$b
  b=$fn
done
echo
