#Leah Oswald
#2420610
#Collaboration: none


#Program that adds up items and displays a total.
#Prompt user to enter quantity of item or 0 to quit.
#Prompt user to enter price of item.
#Calculate subtotal for items.
#Display subtotal for items.
#Calculate the total of all items.
#Display the total.

def main():
    #assign value to variable total and sub_total
    total = 0
    sub_total = 0
    #prompt user to enter quantity and assign to variable quantity
    quantity = int(input('Enter the quantity or 0 quit: '))
    #create while loop that ends if the user enters 0 for quantity
    while quantity != 0:
        #prompt user to enter the price of the item and assign to variable unit_price
        unit_price = float(input('Enter the unit price: '))
        #multiply quantity by unit_price and assign to variable sub_total
        sub_total = quantity * unit_price
        #display subtotal of item
        print('Subtotal for this item: $', format(sub_total, ',.2f'), sep='')
        #calculate running total by adding sub_total to total
        total = total + sub_total
        #prompt user to enter quantity and assign to variable quantity
        quantity = int(input('Enter the quantity or 0 to quit: '))
    #display the total of all items    
    print('Total is $', format(total, ',.2f'), sep='')

#run program    
main()
