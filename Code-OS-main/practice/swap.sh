read -p "a = " a
read -p "b = " b

echo Before Swap
echo a= $a
echo b= $b

a=$((a^b))
b=$((b^a))
a=$((a^b))

echo After Swap
echo a= $a
echo b= $b
