# Leah Oswald
# SPC ID #2420610

# collaboration: none.

#This program converts an improper fraction to a mixed number.
def main():
    
    #prompt the user for the numerator and assign to variable numerator
    numerator = int(input('Enter the numerator '))
    #prompt the user for the denominator and assign to variable demoniator
    denominator = int(input('Enter the demoniator '))
    #divide the numerator by the denominator and assign to variable whole
    whole = numerator // denominator
    #divide the numerator by the denominator and assign remainder to variable remainder
    remainder = numerator % denominator
    #display the mixed number and its remainder
    print('The mixed number is ', whole, ' and ', remainder, '/', denominator, sep='')
main()
