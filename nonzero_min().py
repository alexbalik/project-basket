from numpy import zeros

column1 = zeros([8,1], int)

column1[0] = 0 
column1[1] = 0  
column1[2] = 7 
column1[3] = 0 
column1[4] = 4 
column1[5] = 5
column1[6] = 1
column1[7] = 0


#the below for loop takes the first element of the array as the minimum variable
#and compares with other "test elements" of the array. if the test
#element is smaller it takes over as the new minimum variable

def nonzero_min(from_column):
    min_var = from_column[0] #take the first element of the array
    column_length = len(from_column)
    for index in range(1, column_length): #start from 1 to length1, not 0 to length1
                                          #because otherwise, with the definition of test_ele below,
                                          #we'd be comparing min_var with itself (i.e. min_var = test_ele
                                          #for every iteration.
        test_ele = from_column[index]
        if min_var < test_ele and min_var !=0: #if min_var is less than and non-zero, keep as min_var
            min_var = min_var
        elif test_ele !=0: #if not, and test_ele is non-zero, make test_ele new min_var
            min_var = test_ele
        print(min_var)

    print("Final", min_var)
    return(min_var)
    return(from_column.index(min_var))


nonzero_min(column1)
    
        





