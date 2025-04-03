#!/bin/bash

is_armstrong() {
    num=$1
    temp=$num
    sum=0
    n=${#num}

    while [ "$temp" -gt 0 ]; do
        digit=$((temp % 10))
        sum=$((sum + digit**n))
        temp=$((temp / 10))
    done

    if [ "$sum" -eq "$num" ]; then
        echo "$num is an Armstrong number."
    else
        echo "$num is not an Armstrong number."
    fi
}

read -p "Enter a number: " number
is_armstrong "$number"
