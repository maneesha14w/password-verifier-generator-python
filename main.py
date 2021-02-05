import random 
import string


user_input = input("Please enter 'g' to generate 'v' to verify: ").lower()
print(user_input)

for i in range (random.randint(5,15)):
    print('Num' , i)