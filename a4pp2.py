#Leah Oswald
#2420610
#Collaboration: none

#A program that prompts user to enter integers and decides if they are even or odd until user enters 0.
def main():
#Prompt user to enter an integer or zero, assign to variable number.
    number = int(input('Enter an integer or enter 0 to quit: '))
#When number entered is not zero continue to if number is even or odd.
#When number is zero quit the program.
    while number != 0:
#If the remainder of number divided by 2 is 0 print out that number was even.
        if number % 2 == 0:
            print(number, 'is an even number.')
#If the remainder was not zero print that number is odd.
        else:
            print(number, 'is an odd number.')
#Prompt user to enter another integer or zero, assign to variable number.
        number = int(input('Enter an integer or enter 0 to quit: '))
    print('All done!')
                     
main()
