#Leah Oswald
#2420610
#Collaboration: none

#Program that uses a for loop to cycle through integers 500 to 1000.
#Find multiples of 79.
#Print multiples of 79 on one line 7 characters wide.
#Calculate the total of the multiples.
#Decide if number is even
#Count the number of even multiples of 79.
#If not even add to the count of odd multiples of 79.
#Display the results.

def main():
    #assign starting value to variable
    total = 0
    even_num = 0
    odd_num = 0
    #start a for loop and determine range
    for number in range(500, 1001):
        #calculate if a number is a multiple of 79
        if number % 79 == 0:
            #display all multiples on one line 7 characters wide
            print(format(number, '7d'), end = '')
            #calculate the running total of all the multiples
            total += number
            #decide if a number is even
            if number % 2 == 0:
                #add to even_num running total
                even_num +=1
            #if not even, add to odd_num running total    
            else:
                odd_num +=1
    #display results            
    print('\n\nTotal of multiples:', total, '\nNumber of even multiples:', even_num, '\nNumber of odd multiples:', odd_num)
main()
        
