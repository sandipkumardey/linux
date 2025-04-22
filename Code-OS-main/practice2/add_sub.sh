echo "Calculator"

cal() {
    case $c in
        "+")
            read -p "Enter two numbers: " a b
            echo "$a + $b = $(($a + $b))"
            ;;
        "-")
            read -p "Enter two numbers: " a b
            echo "$a - $b = $(($a - $b))"
            ;;
        "*")
            read -p "Enter two numbers: " a b
            echo "$a * $b = $(($a * $b))"
            ;;
        "/")
            read -p "Enter two numbers: " a b
            echo "$a / $b = $(($a / $b))"
            ;;
        *)
            echo "Invalid choice"
            ;;
    esac
}

echo "choose: 1. (+), 2. (-), 3. (*), 4. (/)"
read -p "Enter your Choice(1, 2, 3, 4): " c

cal 