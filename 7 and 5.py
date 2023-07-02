# Find numbers which re divisible by 7 and multiple of 5 between a given range
m = int(input())
n = int(input())
x = m

while x <= n:

    if(x % 35 == 0):
        print(x)

    x += 1
