# Leah Oswald
# SPC ID# 2420610

#collaboration: none.

# program that gets users first name, last name, and age then displays it
def main():
    # get users first name and assign to variable first_name
    first_name = input('What is your first name? ')
    # get users last name and assign to variable last_name
    last_name = input('What is your last name? ')
    # get users age as an integer and assign to variable years_old
    years_old = int(input('How many years old are you? '))
    # display users name and age
    print('My name is', first_name, last_name, 'and I am', years_old, 'years old.')

main()
