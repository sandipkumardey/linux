echo -n "Enter first number: "
read a
echo -n "Enter second number: "
read b
echo "Before swapping: a = $a, b = $b"
temp=$a
a=$b
b=$temp
echo "After swapping: a = $a, b = $b"