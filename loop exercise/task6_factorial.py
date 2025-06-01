#write a code to print the factorial of given number

user_input = int(input("Enter a value:>"))
print(f'Factorial of {user_input} is:')

fact = 1
for i in range(1, user_input+1):
    fact *= i

print(fact)