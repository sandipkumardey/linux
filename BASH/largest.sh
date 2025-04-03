echo "Enter three numbers: "
read a b c

if [ $a -ge $b ] && [ $a -ge $c ]; then
    echo "Largest: $a"
elif [ $b -ge $a ] && [ $b -ge $c ]; then
    echo "Largest: $b"
else
    echo "Largest: $c"
fi