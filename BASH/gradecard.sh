#!/bin/bash

echo "Student Name:"
echo "Enter the marks (0-100):"
read marks

if ((marks >= 91 && marks <= 100)); then
    grade="O"
elif ((marks >= 81 && marks <= 90)); then
    grade="A+"
elif ((marks >= 71 && marks <= 80)); then
    grade="A"
elif ((marks >= 61 && marks <= 70)); then
    grade="B+"
elif ((marks >= 51 && marks <= 60)); then
    grade="B"
elif ((marks >= 41 && marks <= 50)); then
    grade="C+"
elif ((marks >= 35 && marks <= 40)); then
    grade="C"
else
    grade="F"
fi

echo "Your grade is: $grade"

