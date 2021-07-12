#Leah Oswald
#2420610

#Collaboration: none

import math

#define a function with three arguments 
def wall(length, width, height):
    #calculate total area
    total_area = (length * height) + (width * height)
    total_area2 = total_area * 2
    #return the value
    return total_area2

#define a function with three arguments
def final_area(area, price, cover):
    #calculate how many pails and round up if not equal
    pails = math.ceil(area / cover)
    #calculate the cost of paint
    cost = pails * price
    #display results
    print('This job requires', pails, 'pails of paint.')    
    print('The cost of paint is $', format(cost, ',.2f'), '.',  sep = '')
