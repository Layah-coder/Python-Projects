# Leah Oswald
# COP1000

def main ():
    # get first test score, assign to variable test1
    test1 = int(input('Enter first test score: '))
    # get second test score, assign to variable test2
    test2 = int(input('Enter second test score: '))
    # get third test score, assign to variable test3
    test3 = int(input('Enter third test score: '))
    # add together test1, test2, and test3, assign to variable total
    total = test1 + test2 + test3
    # divide total by 3, assign to variable avg_test_score
    average = total / 3
    # display average
    # sep='' cancels space between print items
    print ('The average of these scores is ',format(average,'.2f'),'%',sep='')

 
main ()
