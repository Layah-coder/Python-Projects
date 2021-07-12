#Leah Oswald
#2420610
#Collaboration: none

# A program that generates random numbers for a list.
# Define a function that that changes one list to a smaller list.
# Prints the number of steps in the list.
# The function then returns the sorted list.
# Define a main function to create a list of random integers and prints it on one line.
# Main function then displays the 4th, 9th and smallest element in the list.
# Finally the main function will call the change_list function and display the results.

#needed to generate random integers
import random


#define change_list with the list numbers
def change_list(numbers):
    #create variable number2 and assign it the elements from 3 to 9(middle 6)
    #can also use [3:-3]
    numbers2 = numbers[3:9]
    #display the number of elements in the new list
    print('The size of the list is now', len(numbers2))
    #return the new list sorted in ascending order
    return sorted(numbers2)

#define the main function
def main():
    #create list numbers
    numbers = []
    print('Here is a list of random integers...')
    #create first for loop that continues to add random integers to list till 12 is reached
    for n in range(12):     
        numbers.append(random.randint(50, 100))
    #create second for loop that prints the integers of the list numbers on one line    
    for num in numbers:
        print(num,end=' ')
    #display the results to the user
    print()
    print('The 4th element in the list is', numbers[3])
    print('The element at index 9 is', numbers[9])
    print('The smallest element in the list is', min(numbers))
    #call change_list(numbers) and assign to new_list
    new_list = change_list(numbers)
    print('change_list returned this sorted list...')
    #display the results of new_list with another for loop on one line
    for num in new_list:
        print(num, end= ' ')






main()
