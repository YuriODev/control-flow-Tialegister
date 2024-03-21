# Your solution to Exercise 12

number = input("Enter a four-digit number: ")

new_number = ""
for digit in number:
    if int(digit) % 2 == 0:
        new_number += "*"
    else:
        new_number += digit
print(new_number)