#import vpython
#ball = vpython.sphere() #note that sphere() is a method that is a part of vpython library
#while True:
#    pass

#above is the long tedious way of using a method in the vpython library

from vpython import * #imports all the methods at once
from time import * #import the time library
floor = box(pos = vector(0, -5, 0), color = color.white, length = 10, height = .1, width = 10)
ceiling = box(pos = vector(0, 5, 0), color = color.white, length = 10, height = .1, width = 10)
leftWall = box(pos = vector(-5, 0, 0), color = color.white, length = .1, height = 10, width = 10)
rightWall = box(pos = vector(5, 0, 0), color = color.white, length = .1, height = 10, width = 10)
backWall = box(pos = vector(0, 0, -5), color = color.white, length = 10, height = 10, width = .1)
marble = sphere(pos = vector(0, -4, 0), color = color.red, radius = 1)
while True:
    pass
