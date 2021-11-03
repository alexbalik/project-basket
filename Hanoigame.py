#Below is the in-progress code that will ultimately allow a user
#to play a game called "Tower of Hanoi". There rules are simple and can be
#found here http://www.carbondalenewschool.com/documents/lg_games/Hanoi%20Tower.pdf

#The program will allow the user to input integers giving instructions
#on where to move the pieces. The program will keep a visible record
#of each move so the user can see emerging patterns, and discover
#the algorithm that beats the game.

#The game will be set up with three column vectors representing each prong,
#with integers elements in the vectors representing the game pieces.

from numpy import zeros
import numpy as np
column1 = zeros([8,1], int) #8x1 vectors with all zeros

column2 = zeros([8,1], int) #8x1 vectors with all zeros

column3 = zeros([8,1], int) #8x1 vectors with all zeros


# replaced column1 zeros with the numbers 1-8.


column1[0] = 1
column1[1] = 2
column1[2] = 3
column1[3] = 4
column1[4] = 5
column1[5] = 6
column1[6] = 7
column1[7] = 8


#pre-defined functions:
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------

#the below function takes the first element of the array as the minimum variable
#and compares with other "test elements" of the array. if the test
#element is smaller it takes over as the new minimum variable
def nonzero_min(from_column):
    min_var = from_column[0] #take the first element of the array
    column_length = len(from_column)
    for index in range(1, column_length): #start from 1 to length1, not 0 to length1
                                          #because otherwise, with the definition of test_ele below,
                                          #we'd be comparing minVar with itself (i.e. min_var = test_ele
                                          #for every iteration.
        test_ele = from_column[index]
        if min_var < test_ele and min_var !=0: #if min_var is less than and non-zero, keep as min_var
            min_var = min_var
        elif test_ele !=0: #if not, and test_ele is non-zero, make test_ele new minVar
            min_var = test_ele
        
    return(min_var)
    return(from_column.index(min_var))



#find lowest index value of a column that is non-zero
def min_index (target_column):
    target_length = len(target_column)
    #we want to look at the range of target column index values
    #we also want the lowest target index that is non-zero
    for target_index in range(0, target_length): #you tried "... in target_length" but
                                                 #target_length isn't an array, it's just
                                                  #an integer!!
        target_ele = target_column[target_index]
        if target_ele == 0:
            continue
        else:
            break
    return(target_ele)


#the block below just detects the index value of an element
def indexof(element):
    lengthof = len(column1)
    for item in range(0, lengthof):
        if column1[item]==element:
            break 
    return(item)

#******end of pre-defined functions********
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------

def update_board(move_from, move_to): #user specifies  origin and target columns

    if move_from == 1: #if user specifies column1. Now user can either move the top element
                       #to column 2 or 3
        
        minvar_global = nonzero_min(column1) #calling function that returns the lowest integer
                                             #value of column1.

        if move_to == 2:
            top_ele = min_index(column2) #calling function that returns top non-zero element of
            index1 = indexof(minvar_global)
            index2 = indexof(top_ele) #calling function that returns top_ele index value of specified column
            
            if top_ele == 0:#if top_ele = 0, put the element at the bottom of the array/prong
                column2[index2] = minvar_global
                column1[index1] = 0
                print(np.c_[column1, column2, column3])
                return(print("Your move has been recorded"))
            
            elif minvar_global < top_ele: #if true, then user made a legal move
                #next, take the index value of the top element, and place
                #minvar_global one index value below (i.e. on top of) top_ele
                column2[index2 - 1] = minvar_global #place minvar_global in column 2
                column1[index1] = 0 #fill in blank space in column1 with a 0
                print(np.c_[column1, column2, column3])
                return(print("Your move has been recorded"))


            elif minvar_global > top_ele: #if true, user made illegal move
                print(np.c_[column1, column2, column3])
                return(print("Sorry, you have made an illegal move."))

x = int(input("Move from which column? Enter an integer: 1, 2, or 3:"))
y = int(input("Move to which column? Enter an integer: 1, 2, or 3:"))
update_board(x, y)








                
                
                
                
                
            
        
        






    
    



