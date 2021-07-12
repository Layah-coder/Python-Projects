# Leah Oswald
# 2420610
# collaboration: none

#A program that prints a table with numbers, their square's, and cube's.
def main():
#Set limitations on the range and increments.
    for number in range(5, 51, 5):
#Calculate the square of number and assign to variable squared.
        squared = number**2
#Calculate the cube of number and assign to variable cubed.
        cubed = number**3
#Display results in a table 7 characters wide.
        print(format(number, '7,d'), format(squared, '7,d'), format(cubed, '7,d'))





main()
