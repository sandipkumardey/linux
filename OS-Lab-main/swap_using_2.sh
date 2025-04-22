echo -n "Enter first number: "
read a
echo -n "Enter second number: "
read b
echo "Before swapping: a = $a, b = $b"
a=$(( $a + $b ))
b=$(( $a - $b ))
a=$(( $a - $b ))
echo "After swapping: a = $a, b = $b"