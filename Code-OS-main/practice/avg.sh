read -p "Enter Three Numbers: " num1 num2 num3

avg=$(echo "scale=2; ($num1+$num2+$num3)/3"|bc)
echo $avg