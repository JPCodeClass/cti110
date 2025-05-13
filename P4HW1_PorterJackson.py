#Jackson Porter
#4/13/2025
#P4HW1
#The users inputs scores, the program stores them, and gives the output to the user



#Start Score List
score_list = int(input('How many scores do you want to enter? '))

scores = []

#Check for valid scores
for i in range(score_list):
    score = int(input(f"Enter score #{i + 1}: "))
    while score < 0 or score > 100:
        print('INVALID Score entered!!!')
        print('Score should be between 0 and 100')
        score = int(input(f"Enter score #{i + 1} again: "))
    scores.append(score)

#Low Score, Drop Lowest, Average New List
low_score = min(scores)
scores.remove(low_score)
average = sum(scores) / len(scores)

#Print Results
print('---------Results---------')
print(f"{'Lowest Score':15} : {low_score}")
print(f"{'Modified List':15} : {scores}")
print(f"{'Scores Average':15} : {average:.2f}")
if average >= 90:
    print('Grade: A')
elif average >= 80:
    print('Grade: B')
elif average >= 70:
    print('Grade: C')
elif average >= 60:
    print('Grade: D')
else:
    print('Grade: F')

#Pseudocode
#As users imput the scores they are stored in a list
#If the score is below 0 or above 100, the user is notified and asked to reenter, that invalid score is dropped
#Finally we call to the list to find the lowesst score, drop it, present a modified list, average the new list and grade on a 10 point scale


