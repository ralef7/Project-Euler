def fib(n):
    sum = 0
    a = 0
    b = 1
    c = 1

    for num in range(n):
        a = b
        b = c
        c = a + b

        num -= 1
        if a < 4000000 and a % 2 == 0:
            sum += a
    return sum
    

print(fib(1000))



    

