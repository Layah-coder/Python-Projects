#Leah Oswald
#2420610
#Collaboration: none

#Program that prompts user to imput friends names/ages and saves them in a file.
#Secondly program will notify user then the file has been created.
def main():
#open friends file and assign to ff
    ff = open('friends.txt', 'w')
    #while loop to get user input
    while True:
        name = str(input('Enter first name of friend or Enter to quit '))
        #if statement to allow user to quit
        if name == '':
            break
        #prompt user for age of friend
        age = int(input('Enter age (integer) of this friend '))
        #write name and age to text file
        ff.write(name + '\n')
        ff.write(str(age) + '\n')
    #close file
    ff.close()
    #display that the file was created
    print('File was created')

main()
