read -p "Enter two numbers: " a b
a=$((a + b))
b=$((a - b))
a=$((a - b))
echo "a = $a, b = $b"
