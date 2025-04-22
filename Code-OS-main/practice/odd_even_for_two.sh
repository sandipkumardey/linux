read -p "Enter two numbers: " a b

if [ $((a & 1)) -eq 0 ] && [ $((b & 1)) -eq 0 ]; then
echo "a and b are even"
elif [ $((a & 1)) -ne 0 ] && [ $((b & 1)) -ne 0 ]; then
echo "a and b are odd"
else
echo Cannot determine
fi
