#Leah Oswald
#2420610
#Collaboration: none

# Program that Chica Chic will use to store invetory data in a file.
# Create a file for inventory to manage data inputs.
# Prompt user for data and write to file.
# Close file.
# Display results.


def main():
    #create a file to write in
    file = open('inven.txt', 'w')
    #prompt user to enter name of first item
    item = input('Enter the name of the inventory item or ENTER to quit ')
    #Start loop that runs till user presses enter to quit
    while item != '':
        #prompt user to price of item and assign to variable price
        price = float(input('Enter the cost price of this item '))
        #prompt user for number of item in stock and assign to variable stock
        stock = int(input('Enter the quantity in stock of this item '))
        #write item, price, and stock into file as strings on own lines
        file.write(item + '\n')
        file.write(str(price) + '\n')
        file.write(str(stock) + '\n')
        #notify that a record was written to file
        print('A record was written to file')
        #prompt user if they need to enter another item or quit
        item = input('Enter the name of the inventory item or ENTER to quit ')
    #close file
    file.close()
    
    #notify user that the file was created and closed
    print('The file was created successfully and closed')
    
main()
    
