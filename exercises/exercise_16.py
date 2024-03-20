# Your solution to Exercise 16


day = int(input("Enter the day: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))

if day == 1:
    if month == 1:
        day = 31
        month = 12
        year -= 1
    else:
        day = 30
        month -= 1
else:
    day -= 1

print(f"{day}.{month}.{year}")