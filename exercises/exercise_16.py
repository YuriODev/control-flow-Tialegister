# Your solution to Exercise 16


day = int(input())
month = int(input())
year = int(input())

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