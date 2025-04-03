echo "Enter x and y: "
read x y

echo "Before: x=$x, y=$y"

x=$((x + y))
y=$((x - y))
x=$((x - y))

echo "After: x=$x, y=$y"
