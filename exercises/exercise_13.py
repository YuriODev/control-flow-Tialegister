# Your solution to Exercise 13

n = int(input())
digits = set(str(n))
if len(digits) == len(str(n)):
    print("True")
else:
    print("False")