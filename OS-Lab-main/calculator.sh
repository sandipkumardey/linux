echo "Simple Calculator"
echo "1. Addition"
echo "2. Subtraction"
echo "3. Multiplication"
echo "4. Division"
echo "5. Exit"

while true
do
    echo -n "Enter your choice (1-5): " 
    read choice

    case $choice in
        1)
            echo -n "Enter first number: " 
            read num1
            echo -n "Enter second number: " 
            read num2
            echo "Result: $((num1 + num2))"
            ;;
        2)
            echo -n "Enter first number: " 
            read num1
            echo -n "Enter second number: " 
            read num2
            echo "Result: $((num1 - num2))"
            ;;
        3)
            echo -n "Enter first number: " 
            read num1
            echo -n "Enter second number: " 
            read num2
            echo "Result: $((num1 * num2))"
            ;;
        4)
            echo -n "Enter first number: " 
            read num1
            echo -n "Enter second number: " 
            read num2
            if [ $num2 -ne 0 ]; then
                echo "Result: $(bc -l <<< "scale=2; $num1 / $num2")"
            else
                echo "Error: Division by zero is not allowed."
            fi
            ;;
        5)
            exit 0
            ;;
        *)
            echo "Invalid choice. Please choose a valid option."
            ;;
    esac
done