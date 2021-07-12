#Leah Oswald
#2420610
#Collaboration: none

#Program that reads file and calculates the average of friends ages.
#Open file.
#Use while loop to read through lines and calculate average.
#Close file.
#Display results.

def main():
    #assing values to total(accumulator) and count(counter)
    total = 0
    count = 0
    #open file and assign to friends
    friends = open('friends.txt', 'r')
    #read line(priming read)
    line = friends.readline()
    #stop while loop if file reaches a blank line, continue while loop if line is not blank
    while line != '':
        #remove /n from each line
        name = line.rstrip('\n')        
        #covert string to int and assign to variable age_sum
        age = int(friends.readline())
        #display friend with age from file
        print('My friend', name, 'is', age)
        #keep count of friends
        count += 1
        #keep total of friends ages
        total += age
        #read next line
        line = friends.readline()
    #close file    
    friends.close()
    #display results
    print('Average age of friends is', format(total / count, '.1f'))


    

main()
