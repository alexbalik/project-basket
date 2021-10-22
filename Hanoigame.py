#Below is the in-progress code that will ultimately allow a user
#to play a game called "Tower of Hanoi". There rules are simple and can be
#found here http://www.carbondalenewschool.com/documents/lg_games/Hanoi%20Tower.pdf

#The program will allow the user to input integers giving instructions
#on where to move the pieces. The program will keep a visible record
#of each move so the user can see emerging patterns, and discover
#the algorithm that beats the game.

#The game will be set up with  three column vectors representing each prong,
#with integers elements in the vectors representing the game pieces.


from numpy import zeros

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


def updateBoard(move_from): #user specifies which column he/she is taking an element from
    move_from = int(input("Move from which column? Enter an integer: 1, 2, or 3:"))

    if move_from == 1: #if user specifies column1. Now user can either move the top element
                       #element to column 2 or 3
        #now we only worry about column1
        move_to = int(input("Move to which column? Enter an integer: 1, 2, or 3:"))
        #^ask user which column to move to
        minvar_global = nonzero_min(column1) # calling function that returns min_var of column1
                                             #(i.e. the top element).

        if move_to == 2:
            top_ele = min_index(column2) #calling function that returns top non-zero element of
                                         #specified column
            
            if minvar_global < top_ele #if true, then user made a legal move
                #next, need the index value of element in column 2, so that
                #the original element can be placed on top of the column 2
                #element.
                
                
            
        
        






    
    



