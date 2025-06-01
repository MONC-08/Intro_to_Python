# Can you remember how to check if a key exists in a dictionary?
# Using the capitals dictionary below write some code to ask the user to input
# a country, then check to see if that country is in the dictionary and if it is
# print the capital. If not tell the user it's not there.

capitals = {'France':'Paris','Spain':'Madrid','United Kingdom':'London',
           'India':'New Delhi','United States':'Washington DC','Italy':'Rome',
           'Denmark':'Copenhagen','Germany':'Berlin','Greece':'Athens',
           'Bulgaria':'Sofia','Ireland':'Dublin','Mexico':'Mexico City'
           }

user_input = input("Which country would you like to check? :> ")
user_input = user_input.lower()

while(not user_input.isalpha()):
    print("Input must be a string.")
    user_input = input("Which country would you like to check? :> ")
    
user_input = user_input.title()
if user_input in capitals:
    print(f'The capital of this {user_input} is {capitals[user_input]}')
else:
    print("No data available.")

