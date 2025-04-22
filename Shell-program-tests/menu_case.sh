#!/bin/bash

while true; do
  echo "1. Check positive/negative/zero"
  echo "2. Display factorial"
  echo "3. Exit"
  read -p "Enter choice: " choice

  case $choice in
    1)
      read -p "Enter number: " num
      if (( num > 0 )); then echo "Positive"
      elif (( num < 0 )); then echo "Negative"
      else echo "Zero"
      fi
      ;;
    2)
      read -p "Enter number: " n
      fact=1
      for (( i=1; i<=n; i++ )); do
        fact=$((fact * i))
      done
      echo "Factorial: $fact"
      ;;
    3)
      echo "Exiting..."; exit 0 ;;
    *)
      echo "Invalid choice" ;;
  esac
done
