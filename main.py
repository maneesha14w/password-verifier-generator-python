import random 
import string

def generatePass():
    for i in range (random.randint(0,9)):
        num_arr = [].append(i)
        str_upper_arr = [].append(random.choice(string.ascii_uppercase))
        str_lower_arr = [].append(random.choice(string.ascii_lowercase))
        
def verifyPass():
    print('')



    while True:             
        user_input = input("Please enter 'g' to generate 'v' to verify: ").lower()
        if user_input == 'g':
            generatePass()
            break
        elif user_input == 'v':
            verifyPass()
            break
        else:
            print("OOps, Please enter 'g' or 'v'")
            continue
        
