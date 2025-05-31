word = input("Enter the string: ")

reverse_string = ''
for ch in word:
    reverse_string = ch + reverse_string

print(reverse_string)

#------------ or -----------------
#print(word[::-1]) ##shortcut