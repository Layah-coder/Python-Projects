#Leah Oswald
#2420610

#collaboration: none

#A program that gets dimensions and values from user and imports functions from another module.
#import custommodule to make functions available
import custommodule

#define main function
def main():
    #prompt user to enter length and assign to variable length
    length = float(input('Enter the length of the room in feet: '))
    #prompt user to enter width and assign to variable width
    width = float(input('Enter the width of the room in feet: '))
    #prompt user to enter height and assign to variable height
    height = float(input('Enter the height of the walls in feet: '))
    #prompt user to enter the price of one pail and assign to variable price
    price = float(input('Enter the price of one pail of paint: '))
    #prompt user to enter how many sq ft one pail covers and assign to variable cover
    cover = float(input('Enter the sq ft covered by one pail: '))
    
    #use custommodule function wall(length, width, height) and assign return value to variable area
    area = custommodule.wall(length, width, height)
    #use custommodule function final_area(area, price, cover) 
    custommodule.final_area(area, price, cover)


#run program
main()
