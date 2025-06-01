
# Write python code that will create a dictionary containing key, value pairs
# that represent the first 10 values of the Fibonacci sequence 
# i.e {1:0,2:1,3:1,4:2,5:3,6:5,7:8 etc}

n = 10
a = 0
b = 1
fibo = dict()

for i in range(1, n+1):
    fibo[i] = a
    a, b = b, a+b

print(fibo)