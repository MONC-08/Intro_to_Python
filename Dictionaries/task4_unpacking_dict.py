# Create a dictoinary containing as keys the letters from A-Z, the values should 
# be random numbers created from the random module. Can you draw a bar graph of 
# the results?


import random

keys = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

d = {}
for letter in keys:
    d[letter] = random.randint(1, 100)

print(d)

import matplotlib.pyplot as plt

x, y = zip(*d.items())
plt.bar(x, y)
