#Leah Oswald
#2420610
#Collaboration: none

# A program to keep track of friends.
# Creates a list to put names enter by user.
# Display to user how many friends are in the list.
# Inserts a name in the beginnning of the list.
# Display friends names on one line.
# Remove a friend from the list.
# Sort the list in alphabetical order.
# Display the remaining friends.

def main():
    #create empty list
    mylist = []
    #prompt user to enter first name of friend
    name = input('Enter the first name of a friend or ENTER to quit ')
    #create while loop to allow user to add friends or quit
    while name != '':
        #add names to list
        mylist.append(name)
        name = input('Enter the first name of a friend or ENTER to quit ')
    #display size of list    
    print('You made a list of', len(mylist), 'friends.')
    print('OOPS, you forgot to enter a very good friend.')
    #use 'if, not in' to search for friend named Wendy
    if 'Wendy' not in mylist:
        #inset Wendy into the start of mylist
        mylist.insert(0, 'Wendy')
        print('If she is not in the list, she will be added now at the start of the list')
    print() 
    print('Here are my friends...')
    #ue for loop to display list of friends on one line
    for friend in mylist:
        print(friend,end=' ')
        
    print('\n')
    #decide which friend moved
    search = (mylist[-1])
    if search in mylist:
        print('Sadly, one friend moved away and was deleted.')
        
        #remove friend from mylist
        mylist.remove(search)
    print('Here are my remaining friends in alphabetical order...')
    #sort list
    mylist.sort()
    #use for loop to display remaining friends on one line
    for friend in mylist:
      print(friend, end=' ')

main()
