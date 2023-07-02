# Write a python program to construct the following pattern, using a nested for Lookup 
# *
# *  *
# *  *  *
# *  *  *  *
# *  *  *  *  *
# *  *  *  *
# *  *  *
# *  *
# *
H = 5

for i in range(1,2*H):
  if i > H:
    i = 2*H - i
  for j in range(i):
    print("*",end = "  ")
   
  print("")
