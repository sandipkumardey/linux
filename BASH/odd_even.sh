echo "enter a number for a= "
read a
r = 'expr $a % 2'
if [ $r -qu o ]
then
 echo "a is even"
else
 echo "a is odd"
fi
