# Your solution to Exercise 9

number = int(input("Enter a three-digit integer: "))

first_digit = number // 100
second_digit = (number // 10) % 10
last_digit = number % 10

sum_of_first_and_last_digits = first_digit + last_digit

if sum_of_first_and_last_digits > second_digit:
    print(">")
elif sum_of_first_and_last_digits < second_digit:
    print("<")
else:
    print("=")