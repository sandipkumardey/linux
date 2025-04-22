echo -n "Enter a number: "
read number
is_prime=1
if (( number <= 1 )); then
    is_prime=0
else
    for (( i=2; i*i<=number; i++ )); do
        if (( number % i == 0 )); then
            is_prime=0
            break
        fi
    done
fi
if (( is_prime == 1 )); then
    echo "$number is a prime number."
else
    echo "$number is not a prime number."
fi