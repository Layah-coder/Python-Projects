# Leah Oswald
# 2020614
# Collaboration: none

#program that asks three different questions and keeps score.
#declare count variable to keep track of correct answers
#Display questions and prompt user for input
#calculate total score and display score to user

def main ():
#declare starting score
    score = 0
#prompt user for input and assign to variable answer1
    answer1 = int(input('How many states are in the continental Unites States? '))
#decide if answer is correct and adjust score if needed
    if answer1 == 48:
        print('Correct!')
        score += 1
    else: 
        print('Incorrect!')
#prompt user for input and assign to variable answer2
    answer2 = float(input('What is the value of pie to 2 decimal places? '))
#decide if answer is correct and adjust score if needed
    if answer2 == 3.14:
        print('Correct!')
        score += 1
    else:
        print('Incorrect!')
#prompt user for input and assign to variable answer3
    answer3= input('What is the capital of Florida (Case sensitive)? ')
#decide if answer is correct and adjust score if needed
    if answer3 == 'Tallahassee':
        print('Correct!')
        score += 1
    else:
        print('Incorrect!')
#display results of quiz
    if score == 3:
        print('Perfect score! ', format(score / 3 *100, '.0f'), '%', sep='')
    elif score == 2:
        print('Almost there! ', format(score / 3 * 100, '.0f'), '%', sep='')
    else:
        print('Try again... ', score,'%', sep='')
main ()
