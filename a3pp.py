# Leah Oswald
# 2420610

# collabaration: none

# Program calculates order totals for coffee sales.

# Named constants to represent coffee prices.
def main():
    LBS_40 = 7.5
    LBS_20 = 8.75
    LBS_10 = 10
    LBS_1 = 12

# Prompt user to enter how many pounds of coffee they want to order and assign to variable quantity.
    quantity = int(input('How many pounds are you ordering? '))

# Determine the cost.
    if quantity >= 40:
        cost = quantity * LBS_40
    elif quantity >= 20:
        cost = quantity * LBS_20
    elif quantity >= 10:
        cost = quantity * LBS_10
    else:
        cost = quantity * LBS_1
# Calculate sales tax and assign to variable tax.
    tax = cost *.07
# Determine shipping cost.
    if cost > 150:
        shipping = 0
    else:
        shipping = quantity * 1
    
# Calculate total and assign to variable total.
    total = cost + tax + shipping
# print cost, tax, shipping, and total.
    print('Cost of coffee $', format(cost, '.2f'), sep='')
    print('7% sales tax $', format(tax, '.2f'), sep='')
    print('Shipping fee $', format(shipping, '.2f'), sep='')
    print('Total Payable $', format(total, '.2f'), sep='')
main()
