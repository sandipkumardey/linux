read -p "Enter the number: " n

flag=0

for ((i=2; i<=n/2; i++)); do
	if ((n % i == 0)); then
		flag=1
		break
	fi
done

if ((flag == 0)); then
	echo "$n is prime"
else
	echo "$n is not prime"
fi
