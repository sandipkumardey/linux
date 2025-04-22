echo -n "Enter a number: "
read num

if [ $((num & 1)) -eq 0 ]
then
    echo "$num is even"
else
    echo "$num is odd"
fi
