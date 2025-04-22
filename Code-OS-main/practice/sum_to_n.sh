read -p "Enter n: " n
sum=0

for((i=0; i<=n; i++)); do
	sum=$((sum+i))
done

echo $sum
