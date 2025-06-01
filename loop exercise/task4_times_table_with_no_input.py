#can you print out the time tables between 1 and 12?
#no need to ask the user for input

for i in range(1, 13):
    print("============================")
    print()
    print(f'This is the {i} times table:')
    print()
    for j in range(1, 13):
        print(f'{i} x {j} = {i*j}')
