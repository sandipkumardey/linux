read -p "Enter the principle: " p
read -p "Enter the rate of interest: " r
read -p "Enter the time(Y): " t
i=$(echo "scale = 2; ($p * $t * $r)/100" | bc)
echo "Interest = $i"

