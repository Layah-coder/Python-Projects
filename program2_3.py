#Leah Oswald
#SPC ID# 2420610

#collaboration: none.

#This program calculates the perimeter and area of a rectangle
import random

def main ():
##    #prompt the user for the length and assign to variable length
##    length = float(input('Enter the length: '))
##    #prompt the user for width and assign to variable width
##    width = float(input('Enter the width: '))
##    #calculate area
##    area = length * width
##    #calculate perimeter
##    perimeter = 2 * (length + width)
##    #output the area
##    print('The area is', format(area, ',.1f'))
##    #output the perimeter
##    print('The perimeter is', format(perimeter, ',.1f'))
##    print(length, 'is', area, 'years of age')

    winter = []
    myfile = open('prices.txt', 'r')
    line = myfile.readline()
    while line != '':
        num = line.rstrip('\n')
        num = float(num)
        winter.append(num)
        line = myfile.readline()
    winter.sort()
    print(len(winter))
    myfile.close()
    for n in winter:
        print(format(n, '.3f'))

main ()
