# Your solution to Exercise 15

day = int(input())
month = int(input())
year = int(input())

if day == 31 and month in [1, 3, 5, 7, 8, 10, 12]:
    day = 1
    month += 1
elif day == 30 and month in [4, 6, 9, 11]:
    day = 1
    month += 1
elif day == 28 or (day == 29 and year % 4 == 0):
    day += 1
else:
    print("Invalid date.")
    exit()

if month == 13:
    month = 1
    year += 1

print(f"{day}.{month}.{year}")