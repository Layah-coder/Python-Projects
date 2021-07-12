#Leah Oswald
#2420610
#Collaboration: none

#Program to get names and ages of friends.
#Then displays how many friends and average age.
#Prompt user to enter friends name.
#Prompt user to enter friends age.
#Display how many friends and the average age of friends.

def main():
    #assign values to variables
    friends = 0
    age_sum = 0
    #create a string  and prompt the user to enter a name or hit enter
    name = str(input('Enter the name of a friend or press ENTER to quit '))
    #use string name to create a while loop
    while name != '':
        #prompt user to enter friends age and assign to variable age
        age = int(input('Enter the age of that friend '))
        #calculate running total of age_sum by adding age to variable age_sum
        age_sum += age
        #calculate running total of friends by adding 1 to variable friends
        friends +=1
        #prompt user again to enter friends name or hit enter to quit
        name = str(input('Enter the name of a friend or press ENTER to quit '))
    #calculate average by dividing age_sum by friends    
    average = age_sum / friends
    #display results
    print('You entered', friends, 'friends')
    print('The average age of your friends is', format(average, '.1f'))

main()
