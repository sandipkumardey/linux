first=5
second=10

first=$((first + second))
second=$((first - second))
first=$((first - second))

echo "After swapping, numbers are:"
echo "first = $first, second = $second"

