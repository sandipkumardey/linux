echo -n "Enter principal amount: "
read p
echo -n "Enter rate of interest: "
read r
echo -n "Enter time in years: "
read t
si=$(( $p * $r * $t / 100))
echo "Simple Interest = $si"