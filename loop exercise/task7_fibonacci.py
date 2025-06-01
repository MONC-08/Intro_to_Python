# Write code to calculate Fibonacci numbers.
# A list containing first 20 fibonacci numbers (0 1 1 2 3 5 8 13 .....)

n = 10
a , b = 0, 1
fibo_nums = []

for i in range(n):
    fibo_nums.append(a)
    a, b = b, a+b

print(f'the fibonacci of {n} is {fibo_nums}')
