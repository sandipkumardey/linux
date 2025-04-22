is_prime() {
    local num=$1
    if [ "$num" -le 1 ]; then
        return 1
    fi
    for ((i=2; i*i<=num; i++)); do
        if [ $((num % i)) -eq 0 ]; then
            return 1
        fi
    done
    return 0
}

for ((num=2; num<=10000; num++)); do
    if is_prime $num; then
        echo $num
    fi
done