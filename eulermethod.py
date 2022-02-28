from numpy import zeros
import numpy as np

#The goal of this program is to use the euler method of approximation in the context of radioactive decay, and graph results. 



#plan: define variables, calculate, store to file, graph


#Here are my two functions that calculate and store.

#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------
#function that actually uses the euler method to make approximation
def calculate(n_uranium, time, tau, t_step, n_steps):
    for i in range(0, n_steps-1): #there are 100 slots labelled 0-99. The user provides the first slot, leaving indices 1-99
        n_uranium[i+1] = n_uranium[i] - (n_uranium[i]/tau)*t_step #skip first index becuase we already know nuclei @ t=0
        time[i+1] = time[i] + t_step # we already know we're starting at t= 0 so skip first index

        #sidenote: in general, n_uranium[j] = number of nuclei at the jth time step.

#function that stores values to file to be used to make a plot
def store(n_uranium, time, n_steps):
    decay = open('decay.txt', 'w')
    for i in range(0, n_steps): #goes through indices 0-99 and write each tuple to a line of the file.
        decay.write(str(n_uranium[i]) + ',' + ' ')
        decay.write(str(time[i]) + '\n')
    decay.close()
#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------


#define variables and prompt user to input values
nuclei = zeros([100], float) #array representing the number of nuclei that has 100 slots
t = zeros([100], float) #array representing the time value corresponding the number of nuclei

t[0] = 0 #set the initial value of time to 0, because we start at 0 and then add time steps
nuclei[0] = float(input("Enter initial number of nuclei: ")) #user enters number of nuclei at t=0

tc = float(input("Enter time constant: "))
dt = float(input("Enter time step: "))
total_time = float(input("Enter total time: "))

n = min([int(total_time/dt), 100]) #number of time steps to calculate (1dt, 2dt, 3dt..., so on)
                                   #100 is the maximum number of time steps we'll consider. So
                                   #if the user enters data such that the number of steps is
                                   #less than 100, this will give (total_time/dt).




#call the functions
calculate(nuclei, t, tc, dt, n)
store(nuclei, t, n)


#test to see if what was written in the file is correct
decay = open('decay.txt', 'r')
print(decay.read())
decay.close()
