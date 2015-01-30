num = 10

x = 2

while x * x <=num:
    while num % x == 0:
        num = num / x

    x+= 1

print(num)
