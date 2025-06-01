#Ask user to input a sequence of numbers.
#Then calculate the mean and print the result.

user_input = input('Enter a number. Type exit to stop :>')
numbers = []

while(user_input.lower() != 'exit'):

    while(not user_input.isdigit()):
        print("That is not a number! Numbers only please: >")
        user_input = input('Try again :')

    numbers.append(int(user_input))
    user_input = input("please enter next number:>")

total = 0
for x in numbers:
    print(x, end = " ")
    total += x
print(f'The calculated mean is: {total/len(numbers)} ')

#=====================================
#print(sum(numbers)/len(numbers)) ##shortcut