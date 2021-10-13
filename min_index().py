from numpy import zeros

column1 = zeros([8,1], int)

column1[0] = 0 
column1[1] = 0  
column1[2] = 0 
column1[3] = 2 
column1[4] = 0 
column1[5] = 5
column1[6] = 1
column1[7] = 0


#below finds the element of an array that is highest up, and non-zero.

def min_index (target_column):
    target_length = len(target_column)
    #we want to look at the range of target column index values
    #we also want the lowest target index that is non-zero
    for target_index in range(0, target_length): #you tried "... in target_length" but
                                                 #target_length isn't an array, it's just
                                                 #an integer!!
        target_ele = target_column[target_index]
        if target_ele == 0: 
            continue #if the element is zero, it is not considered, so restart the loop.
        else:
            break #when we find the first non-zero element starting from the top of the array,
                  #break out of the loop and return that value.
    print("Final", target_ele)
    return(target_ele)

min_index(column1)
            
        





