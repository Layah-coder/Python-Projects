#Leah Oswald
#2420610
#Collaboration: none

#Program that lets user choose how many numbers to generate and their range.
#Define a function that has three arguments.
#Define variables odd, even, total, and num_count.
#Generate random number, determine if even or odd.
#Keep count of even, odd, and total.
#Display results.

#import random module
import random


#create random_number function with three arguments
def random_number(num_int, low_int, high_int):
    #define starting totals for odd, even, total, and num_count
    odd = 0
    even = 0
    total = 0
    num_count = 0
    #for loop starts the count of the number of integers determined by user
    for count_int in range(num_int):
        #while loop decided when loop should stop
        while num_int != num_count:
            num_count += 1
            #generate random number in range determined by user
            num_1 = random.randint(low_int, high_int)
            #display numbers on one line
            print(num_1, ' ', end = '')
            #calculate even, odd, and total
            if num_1 % 2 == 0:
                even += 1
                total += num_1
            else:
                odd += 1
                total += num_1
        #return the values of even, odd, num_int, and total
        return even, odd, num_int, total
            

def main():
    #prompt user for integers and assign to variables num_int, low_int, and high_int
    num_int = int(input('How many integers are to be generated? '))
    low_int = int(input('Enter the lowest integer desired: '))
    high_int = int(input('Enter the highest integer desired: '))
    #call on the random_number function and assign the returned values to variables even_2, odd_2, num_int2, and total_2
    even_2, odd_2, num_int2, total_2 = random_number(num_int, low_int, high_int)
    #display results
    print('\n', even_2, ' of the numbers were even and ', odd_2, ' of the numbers generated were odd', sep = '')
    print('The total of those', num_int2, 'random numbers is', total_2)

    
#run program
main()
