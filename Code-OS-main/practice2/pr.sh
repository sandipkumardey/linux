read -p "Enter the month and the year: " m y

# Check if the year is a leap year
if ((y % 4 == 0 && (y % 100 != 0 || y % 400 == 0))); then
	is_leap_year=1
else
	is_leap_year=0
fi

# Determine the number of days in the month
case $m in
	1|3|5|7|8|10|12)
		echo 31
		;;
	4|6|9|11)
		echo 30
		;;
	2)
		if ((is_leap_year == 1)); then
			echo 29
		else
			echo 28
		fi
		;;
	*)
		echo "Invalid month"
		;;
esac
