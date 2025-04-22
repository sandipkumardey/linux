get_grade() {
    case $1 in
        100|9[0-9]) echo "Grade: A+" ;;
        8[0-9]) echo "Grade: A" ;;
        7[0-9]) echo "Grade: B" ;;
        6[0-9]) echo "Grade: C" ;;
        5[0-9]) echo "Grade: D" ;;
        4[0-9]) echo "Grade: E (Pass)" ;;
        [0-3][0-9]) echo "Grade: F (Fail)" ;;
        *) echo "Invalid average marks!" ;;
    esac
}

is_valid_marks() {
    echo "$1" | grep -qE '^[0-9]+$' && [ "$1" -ge 0 ] && [ "$1" -le 100 ]
}

read -p "Enter marks for Subject 1 (0-100): " sub1
read -p "Enter marks for Subject 2 (0-100): " sub2
read -p "Enter marks for Subject 3 (0-100): " sub3

if ! is_valid_marks "$sub1" || ! is_valid_marks "$sub2" || ! is_valid_marks "$sub3"; then
    echo "Error: Please enter valid numeric marks between 0 and 100."
    exit 1
fi

average=$(( (sub1 + sub2 + sub3) / 3 ))

echo "Average Marks: $average"
get_grade "$average"
