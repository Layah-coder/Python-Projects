#Leah Oswald
#2420610
#collaboration: none

# A program with two functions.
# Create show_list function to display all the integers and accumulate the total of all integers.
# Create main function with an empy list.
# Generate 12 random integers into mylist.
# Sort mylist in descending order.
# Display the largest three integers and smallest three integers in mylist.
# Call show_list.


import random

#define show_list
def show_list(mylist):
    #give value to total accumulator
    total = 0
    #use loop to display all integers in list with a space on one line to user
    for num in mylist:
        print(num, end= ' ')
    #use for loop to accumulate total
    for num in mylist:
        total += num
    print()
    #display results of total to user
    print('The sum for all integers in the list is', total)

#define main functions
def main():
    #create empty list
    mylist = []
    #fill empty list with 12 random integers from 1 up to/including 50
    for n in range (12):
        mylist.append(random.randint(1, 50))
        #sort list in ascending order
        mylist.sort()
        #reverse sort order to descending
        mylist.reverse()
    #create sub-list slice of the largest three integers in mylist    
    large_sub = mylist[0:3]
    #create sub-list slice of the smallest three integers in mylist
    small_sub = mylist[-3:]
    #display bith sub-lists
    print('The largest three integers are', large_sub)
    print('The smallest three integers are', small_sub)
    print('Here are all the integers, sorted from highest to lowest...')
    #call show_list void function
    show_list(mylist)

main()
