#Below is the code that allows a user to play a game called "Tower of Hanoi".
#The goal of the puzzle is to move all the integers from the leftmost column to the
#rightmost column, adhering to one rule:

#A larger integer may not be placed on top of a smaller integer.

#The program prompts the user to input 1,2, or 3 twice each turn. This specifies the original and
#target column of the integer being moved. The program will keep a visible record of each move so
#the user can see emerging patterns, and discover the algorithm that beats the game.

#The game will be set up with three column vectors representing each prong,
#with integers elements in the vectors representing the game pieces.

from numpy import zeros
import numpy as np

column1 = zeros([8,1], int) #8x1 vector with all zeros

column2 = zeros([8,1], int) #8x1 vector with all zeros

column3 = zeros([8,1], int) #8x1 vector with all zeros


# replaced column1 zeros with the numbers 1-8.


column1[0] = 1
column1[1] = 2
column1[2] = 3
column1[3] = 4
column1[4] = 5
column1[5] = 6
column1[6] = 7
column1[7] = 8


#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#user-defined functions:

#find top non-zero element in a given column.
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
def indexof(element_to_find, within):
    lengthof = len(within)
    for index_to_find in range(0, lengthof):
        if within[index_to_find]==element_to_find:
            break 
    return(index_to_find)



#Here are all possible moves. The top row is the original column, and the bottom are possible target columns.
#-----1--------------2---------------------3
#---2   3----------1   3-----------------1   2

def update_board(move_from, move_to): #user specifies origin and target columns

    if move_from == 1: #if, for instance, user specifies column1. Now user can either move the top element
                       #to column 2 or 3
        
        minvar_global = min_index(column1) #calling function that returns the lowest integer
                                             #value of column1.

        if move_to == 2:
            top_ele = min_index(column2) #calling function that returns top non-zero element of specified column.
            index1 = indexof(minvar_global, column1)
            index2 = indexof(top_ele, column2) #returns index value of a given element within specified column.

            if minvar_global == 0:
                return(False)

            elif top_ele == 0:#if top_ele = 0, put the element at the bottom of the array/prong
                column2[7] = minvar_global
                column1[index1] = 0
                return(True)
            
            elif minvar_global < top_ele: #if true, then user made a legal move
                #next, take the index value of the top element, and place
                #minvar_global one index value below (i.e. on top of) top_ele
                column2[index2 - 1] = minvar_global #place minvar_global in column 2
                column1[index1] = 0 #fill in blank space in column1 with a 0
                return(True)


            elif minvar_global > top_ele: #if true, user made illegal move
                return(False)
                

        elif move_to == 3:
            top_ele = min_index(column3) #calling function that returns top non-zero element of specified column.
            index1 = indexof(minvar_global, column1)
            index3 = indexof(top_ele, column3) #returns index value of a given element within specified column.
            
            if minvar_global == 0:
                return(False)

            elif top_ele == 0:#if top_ele = 0, put the element at the bottom of the array/prong
                column3[7] = minvar_global
                column1[index1] = 0
                return(True)
            
            elif minvar_global < top_ele: #if true, then user made a legal move
                #next, take the index value of the top element, and place
                #minvar_global one index value below (i.e. on top of) top_ele
                column3[index3 - 1] = minvar_global #place minvar_global in column 2
                column1[index1] = 0 #fill in blank space in column1 with a 0
                return(True)


            elif minvar_global > top_ele: #if true, user made illegal move
                return(False)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    if move_from == 2: #if user specifies column1. Now user can either move the top element
                       #to column 2 or 3
        
        minvar_global = min_index(column2) #calling function that returns the lowest integer
                                             #value of column2.

        if move_to == 1:
            top_ele = min_index(column1) #calling function that returns top non-zero element of specified column.
            index2 = indexof(minvar_global, column2)
            index1 = indexof(top_ele, column1) #returns index value of a given element within specified column.
            
            if minvar_global == 0:
                return(False)

            elif top_ele == 0:#if top_ele = 0, put the element at the bottom of the array/prong
                column1[7] = minvar_global
                column2[index2] = 0
                print(index2)
                return(True)
            
            elif minvar_global < top_ele: #if true, then user made a legal move
                #next, take the index value of the top element, and place
                #minvar_global one index value below (i.e. on top of) top_ele
                column1[index1 - 1] = minvar_global #place minvar_global in column 2
                column2[index2] = 0 #fill in blank space in column1 with a 0
                return(True)


            elif minvar_global > top_ele: #if true, user made illegal move
                return(False)

        elif move_to == 3:
            top_ele = min_index(column3) #calling function that returns top non-zero element of specified column.
            index2 = indexof(minvar_global, column2)
            index3 = indexof(top_ele, column3) #returns index value of a given element within specified column.
            
            if minvar_global == 0:
                return(False)

            elif top_ele == 0:#if top_ele = 0, put the element at the bottom of the array/prong
                column3[7] = minvar_global
                column2[index2] = 0
                return(True)
            
            elif minvar_global < top_ele: #if true, then user made a legal move
                #next, take the index value of the top element, and place
                #minvar_global one index value below (i.e. on top of) top_ele
                column3[index3 - 1] = minvar_global #place minvar_global in column 2
                column2[index2] = 0 #fill in blank space in column1 with a 0
                return(True)

            elif minvar_global > top_ele: #if true, user made illegal move
                return(False)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    if move_from == 3: #if user specifies column1. Now user can either move the top element
                       #to column 2 or 3
        
        minvar_global = min_index(column3) #calling function that returns the lowest integer
                                             #value of column3.

        if move_to == 1:
            top_ele = min_index(column1) #calling function that returns top non-zero element of specified column.
            index3 = indexof(minvar_global, column3)
            index1 = indexof(top_ele, column1) #returns index value of a given element within specified column.
            
            if minvar_global == 0:
                return(False)

            elif top_ele == 0:#if top_ele = 0, put the element at the bottom of the array/prong
                column1[7] = minvar_global
                column3[index3] = 0
                return(True)
            
            elif minvar_global < top_ele: #if true, then user made a legal move
                #next, take the index value of the top element, and place
                #minvar_global one index value below (i.e. on top of) top_ele
                column1[index1 - 1] = minvar_global #place minvar_global in column 2
                column3[index3] = 0 #fill in blank space in column1 with a 0
                return(True)


            elif minvar_global > top_ele: #if true, user made illegal move
                return(False)

        elif move_to == 2:
            top_ele = min_index(column2) #calling function that returns top non-zero element of specified column.
            index3 = indexof(minvar_global, column3)
            index2 = indexof(top_ele, column2) #returns index value of a given element within specified column.
            
            if minvar_global == 0:
                return(False)

            elif top_ele == 0:#if top_ele = 0, put the element at the bottom of the array/prong
                column2[7] = minvar_global
                column3[index3] = 0
                return(True)
            
            elif minvar_global < top_ele: #if true, then user made a legal move
                #next, take the index value of the top element, and place
                #minvar_global one index value below (i.e. on top of) top_ele
                column2[index2 - 1] = minvar_global #place minvar_global in column 2
                column3[index3] = 0 #fill in blank space in column1 with a 0
                return(True)


            elif minvar_global > top_ele: #if true, user made illegal move
                return(False)
#End of user-defined function
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------


print("Here is your starting board:")
print(np.c_[column1, column2, column3])

movelist = []

for turn in iter(int,1): #iter() keeps iterating until int() returns a value of 1. But int() always returns 0,
                         #so this loop will go on forever.
    x = int(input("Move from which column? Enter an integer: 1, 2, or 3:"))
    y = int(input("Move to which column? Enter an integer: 1, 2, or 3:"))
    if update_board(x, y):
        movelist.append((x,y))
        print('')
        print("Move recorded")
        print(np.c_[column1, column2, column3])
        print(movelist)
        if column3[0] == 1:
            break #the game will only end when column3 is filled. The constraints are such that a column will be
                  #filled if and only if 1 is at the 0th index of that column.
    else:
        print('')
        print("You have made an illegal move")
        print(np.c_[column1, column2, column3])
        print(movelist)
print("Congratulations, you won the game!")
