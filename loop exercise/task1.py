#ask the user for two numbers between 1 and 100. 
#Then count from the lower number to higher. 
# print the result to the screen.

num_1 = int(input("Enter between 1 and 100 >"))
num_2 = int(input("Enter between 1 and 100 >"))

while(num_1 < 1 or num_1 > 100 or num_2 < 1 or num_2 > 100 or num_1 == num_2):
    print("Number must be between 1 and 100. Try again:")
    num_1 = int(input("Enter between 1 and 100 >"))
    num_2 = int(input("Enter between 1 and 100 >"))

if(num_1 > num_2):
    for x in range(num_2, num_1+1):
        print(x, end = " ")
else:
    for x in range(num_1, num_2+1):
        print(x, end = " ")