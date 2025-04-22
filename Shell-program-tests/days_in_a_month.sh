#!/bin/bash
read -p "Enter month (1-12): " month
read -p "Enter year: " year

# Check for leap year
if (( year % 4 == 0 && ( year % 100 != 0 || year % 400 == 0 ) )); then
  leap="yes"
else
  leap="no"
fi

case $month in
  1|3|5|7|8|10|12) days=31 ;;
  4|6|9|11) days=30 ;;
  2)
    if [ "$leap" == "yes" ]; then days=29
    else days=28
    fi
    ;;
  *) echo "Invalid month"; exit 1 ;;
esac

echo "Days: $days"
echo "Leap year: $leap"
