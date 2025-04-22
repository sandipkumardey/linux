read -p "Enter principle: " p
read -p "Enter rate of interest: " r
read -p "Enter year: " t

interest=$(echo "scale=2; (($p * $r * $t)/100)" | bc)

echo $interest
