# Your solution to Exercise 4

School_Grades=int(input())

if School_Grades <= 3:
  print( "initial level ")

elif 3 < School_Grades <=6:
  print("average level")

elif 6 < School_Grades <=9:
  print("sufficient level")

elif 9 < School_Grades <=12:
  print("high level")

else:
  print("level is absent")

