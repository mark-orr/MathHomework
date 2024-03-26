#import pandas as pd
#import matplotlib.pyplot as plt
import numpy as np
import time

'''
# Start timer
start_time = time.time()

# Code to be timed
# ...

# End timer
end_time = time.time()

# Calculate elapsed time
elapsed_time = end_time - start_time
print("Elapsed time: ", elapsed_time) 
'''
for i in range(0,200):
    print(' \n')

'''FIXED DATA STRUCTURES'''
arr_multiplier = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

'''DEFS'''
def generate_table(base,multiplier):
    '''
    base is the times table the kid wants
    multiplier is a np.array (1d) of 1...12
    '''
    return [i for i in base*multiplier]

def play_game(table_kind,multiplier,multiplicand):
    '''
    See above for some inputs
    '''
    # Start timer
    start_time = time.time()
    for i in range(0,len(multiplier)):
        print(multiplier[i],' X ',table_kind, ' = ???')
        user_guess = int(input())
        if user_guess == multiplicand[i]:
            print('CORRECT!')
        else: 
            print('INCORRECT, DUMB DUMB!')
    # End timer
    end_time = time.time()
    return start_time, end_time





'''GET TABLE'''
#query kid
#table_kind = int(input("What Times Table Do You Want?"))
#make table
#arr_multiplicand = generate_table(table_kind,arr_multiplier)
#NOW INDEX IS MATCHED FOR multiplier and multiplicand

def main_game():
    '''PLAY GAME ONE ROUND'''
    #PLAY GAME
    game_on = input("Would you like to play a game? (Y/N): \n")

    if game_on == "Y":
        table_kind = int(input("What Times Table Do You Want? (2 to infinity): \n"))
        #make table
        arr_multiplicand = generate_table(table_kind,arr_multiplier)
        #NOW INDEX IS MATCHED FOR multiplier and multiplicand   
        catch = play_game(table_kind,arr_multiplier,arr_multiplicand)


    elif user_input == "N":
        print("Exiting Game")
        exit()

    else:
        print("You entered an invalid option.\nExiting.")
        exit()
    
    for i in range(0,10):
        print('GAME OVER!') 
    
        # Calculate elapsed time
    elapsed_time = catch[1] - catch[0]
    print("Elapsed time: ", elapsed_time) 
    exit()

if __name__ == '__main__':
    main_game()
#EOF

