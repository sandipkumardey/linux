echo "enter value of first="
read first
echo "enter value of second="
read second

temp=$first
first=$second
second=$temp

echo "After swapping, numbers are:"
echo "first = $first, second = $second"
