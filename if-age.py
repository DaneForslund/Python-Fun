import random
#age = random.randint(1, 150)
age = 15
A = range(12)
B = range(13, 18)
C = range(18, 150)

if age in A:
  print("You are considered a kid.")
if age in B:
  print("You are considered a teenager.")
if age in C:
  print("You are considered an adult.")
  
