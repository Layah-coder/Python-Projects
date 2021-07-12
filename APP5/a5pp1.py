#Leah Oswald
#2420610

#Collaboration: none

#A program that uses a function to compare integers.
#Generate random numbers and asign to variable's num_1 and num_2.
#Assign arguments to function show_larger.
#Assign peremeters to function show_larger.
#Determine if the numbers are egual.
#Determine which number is larger and calculate the difference.

#import random from python library 
import random

#define main program
def main():
    #generate random integer in range of 1-5 and assign to variable num_1
    num_1 = random.randint(1, 6)
    #generate random integer in range of 1-5 and assign to variable num_2
    num_2 = random.randint(1, 6)
    #run function show_larger with arguments num_1, and num_2
    show_larger(num_1, num_2)

#define show_larger function
def show_larger(number_1, number_2):
    #determine if numbers are equal
    if number_1 == number_2:
        #display that numbers are equal
        print('The integers are equal, both are', number_1)
        #return to main
        return
    #if numbers are not equal determine if number_1 is larger
    else:
        if number_1 > number_2:
            #calculate and display the difference
            print(number_1, 'is larger than', number_2, 'by', (number_1 - number_2))
        #if number_1 is not larger display that number_2 is larger and calculate the difference    
        else:
            print(number_2, 'is larger than', number_1, 'by', (number_2 - number_1))



#run program
main()
