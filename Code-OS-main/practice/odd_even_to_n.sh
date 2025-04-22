read -p "Enter n: " n

for ((i=0; i<=n; i++)); do
	if [ $((i % 2)) -eq 0 ]; then
		echo $i
	fi
done
