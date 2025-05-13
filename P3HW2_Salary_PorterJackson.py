#Jackson Porter
#3/30/2025
#P3HW2
#This program takes the users name, hrs worked, and pay rate to calculate overtime, ot pay, regular pay, and gross pay



#Input
name = input("Enter employee's name: ")
hrs_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

#Overtime
if hrs_worked > 40:
    ot = hrs_worked - 40
else:
    ot = 0

#Overtime Pay
ot_pay = ot * (pay_rate * 1.5)

#Base Pay
reghour_pay = hrs_worked * pay_rate - (ot_pay / 1.5)



#Gross Pay
gross_pay = reghour_pay + ot_pay

#Output
print('-------------------------------')
print(f'Employee name:     {name}')
print()
print('Hours Worked   Pay Rate       OverTime       OverTime Pay   RegHour Pay    Gross Pay')
print('-----------------------------------------------------------------------------------------------')
print(f'{hrs_worked:<15.1f}{pay_rate:<15.1f}{ot:<15.1f}{ot_pay:<15.2f}{reghour_pay:<15.2f}{gross_pay:<15.2f}')     



#Pseudocode
#The program starts with user input including name, hours worked, and their hourly pay
#It then calcualtes if any time over 40 hours is worked and takes whatever is over 40 and makes it overtime
#It then takes that overtime and times it but the (pay rate * 1.5) 1.5 being time and a half
#It than calculates base bay by taking the hours wokred times the pay rate minus (overtime pay divided by 1.5). This is done to recalculate and not take away the overtime pay scale from the base pay scale
#It ends with outputting a pay stub for the user
