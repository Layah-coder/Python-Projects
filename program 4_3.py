#Leah Oswald
#2420610
#Collaboration: none

#Program that uses * to make a triangle with nested for loops.
#Start for loop and create variable x.
#Start nested for loop and create variable y, subtract x from 10.
#Display results.

def main():
    #for loop that determines the amount of rows
    for x in range (10):
        #nested for loop to print out how many * per row
        for y in range(10-x):
            print('*', end=' ') 
        print()
main()
    
