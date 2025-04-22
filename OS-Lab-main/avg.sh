echo -n "Enter first number: "
read a
echo -n "Enter second number: "
read b
echo -n "Enter third number: "
read c
avg=$(( ($a + $b + $c) / 3))
echo "Average of $a, $b and $c is $avg"