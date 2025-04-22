echo -n "Enter a number: "
read num

temp=$num
digits=0

while [ $temp -gt 0 ]
do
    temp=$((temp / 10))
    digits=$((digits + 1))
done

temp=$num
sum=0

while [ $temp -gt 0 ]
do
    digit=$((temp % 10))
    power=1
    for ((i = 1; i <= digits; i++))
    do
        power=$((power * digit))
    done
    sum=$((sum + power))
    temp=$((temp / 10))
done

if [ $sum -eq $num ]
then
    echo "$num is an Armstrong number"
else
    echo "$num is not an Armstrong number"
fi