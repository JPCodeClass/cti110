#Jackson Porter
#3/16/2025
#P2HW2
#This program will take the grades entered by the user, and display the lowest, highest, sam, and average of the grades

grades = []

mod1_grade = float(input('Enter grade for Module 1:'))
mod2_grade = float(input('Enter grade for Module 2:'))
mod3_grade = float(input('Enter grade for Module 3:'))
mod4_grade = float(input('Enter grade for Module 4:'))
mod5_grade = float(input('Enter grade for Module 5:'))
mod6_grade = float(input('Enter grade for Module 6:'))

grades.append(mod1_grade)
grades.append(mod2_grade)
grades.append(mod3_grade)
grades.append(mod4_grade)
grades.append(mod5_grade)
grades.append(mod6_grade)

lowest = min(grades)
highest = max(grades)
total = sum(grades)
average = total / 6

print()
print('----------Results----------')
print(f'Lowest Grade:     {lowest:.2f}')
print(f'Highest Grade:    {highest:.2f}')
print(f'Sum of Grades:    {total:.2f}')
print(f'Average:          {average:.2f}')
print('---------------------------')

#Pseudocode
    #First an empty list is created
    #Then the user inputs their 6 grades
    #The the list is appended with the input from the user
    #Then math is done to find the lowest, highest, sum, and average
    #Finally, the results are printed for the user to see
