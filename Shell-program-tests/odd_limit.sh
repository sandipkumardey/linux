#!/bin/bash
read -p "Enter limit: " limit
for (( i=1; i<=limit; i+=2 )); do
  echo "$i"
done
