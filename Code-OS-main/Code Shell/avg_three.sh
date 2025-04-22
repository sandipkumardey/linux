read -p "Enter three numbers: " a b c
avg=$(echo "scale=2; ($a + $b + $c) / 3" | bc)
echo "Result = $avg"

