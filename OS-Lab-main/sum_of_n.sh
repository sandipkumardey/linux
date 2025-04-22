echo -n "Enter threshold: "
read t
for (( i=1; i<=t; i++ ))
    do
        sum=$(( $sum + i ))
    done
echo "Sum of first $t numbers is: $sum"