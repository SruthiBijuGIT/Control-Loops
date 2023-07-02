#Write a program that accepts the lengths of three sides of a triangle as inputs. The program output should indicate whether the triangle is 
#A. Equilateral triangle 
#B. Right angle triangle 
#C. Doesn’t come in both categories
a=int(input())
b=int(input())
c=int(input())
if(a==b and a==c):
 print("Equilateral Triangle")
elif(c**2==((b**2)+(a**2))):
  print("Right Angle Triangle")
else:
  print("Doesn't come in both cases")
