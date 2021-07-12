# Leah Oswald
# 2420610
# Collaboration: none

#Program that calculates and displays a receipt for Mississippi.com.
#Prompt the user for unit price and assign to variable unit_price.
#Prompt the user for quantity and assign to variable quantity.
#Prompt the user if item is taxable and assign to is_taxable.
#Calculate receipt.
#Display results.

def main ():
#prompt for user input
    unit_price = float(input('Enter price of the item: '))
    quantity = int(input('Enter quantity desired: '))
    is_taxable = input('Is the item taxable? Enter T or F (Case sensitive): ')
#calculate cost
    cost = unit_price * quantity
#determine shipping
    if cost >= 50:
        shipping = 0
    else:
        shipping = 7
#determine and calculate tax

    if is_taxable == 'T':
        tax = cost *.07
    else:
        tax = 0
#calculate subtotal
    subtotal = unit_price * quantity
#calculate total
    total = subtotal + shipping + tax
#display results on four lines.
    print('Subtotal $', format(subtotal, ',.2f'), sep='')
    print('Sales tax $', format(tax, ',.2f'), sep='')
    print('Shipping cost $', format(shipping, ',.2f'), sep='')
    print('Total amount due $', format(total, ',.2f'), sep='')                   
main()
