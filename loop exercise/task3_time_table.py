#Ask the user to enter between 1 and 12 
#Then display a times table for that user.

user_input = input("Enter between 1 and 12 :>")
while((not user_input.isdigit()) or int(user_input) < 1 or int(user_input) > 12):
    print("Number must be between 1 and 12:")
    user_input = input("Enter between 1 and 12 :>")

user_input = int(user_input)
print('============================')
print()
print(f'This is the {user_input} times table:')
print()
for i in range(1, 13):
    print(f'{i} x {user_input} = {i*user_input}')