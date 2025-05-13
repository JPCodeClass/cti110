#Jackson Porter
#4/13/2025
#P4HW2
#Program calculates the Employee, Hrs Worked, Pay Rate, Possible OT, and Pay, then can do multiple employees, and show final payments when program is terminated

#Start and Set up Lists
program_start = 0
names = []
totalot = []
totalreg = []
totalgross = []

#Enter Name, Done prtints final totals, If Name entered, get Hrs Worked and Pay Rate
while program_start == 0:
    name = input("Enter employee's name or 'Done' to terminate: ")
    if 'Done' in name:
        print(f"Total amount of employees entered:",len(names))
        print(f"Total amount paid for overtime: ${sum(totalot):.2f}")
        print(f"Total amount paid for regular hours: ${sum(totalreg):.2f}")
        print(f"Total amount paid in gross: ${sum(totalgross):.2f}")
        break
    hrs_worked = float(input(f"How many hours did {name} work? "))
    pay_rate = float(input(f"What is {name}'s pay rate? "))
    if hrs_worked > 40:
        ot = hrs_worked - 40
    else:
        ot = 0
    ot_pay = ot * (pay_rate * 1.5)
    reghour_pay = hrs_worked * pay_rate - (ot_pay / 1.5)
    gross_pay = reghour_pay + ot_pay
    names.append(name)
    totalot.append(ot_pay)
    totalreg.append(reghour_pay)
    totalgross.append(gross_pay)
    print('-------------------------------')
    print(f'Employee name:     {name}')
    print()
    print('Hours Worked   Pay Rate       OverTime       OverTime Pay   RegHour Pay    Gross Pay')
    print('-----------------------------------------------------------------------------------------------')
    print(f'{hrs_worked:<15.1f}{pay_rate:<15.1f}{ot:<15.1f}{ot_pay:<15.2f}{reghour_pay:<15.2f}{gross_pay:<15.2f}')
    print()
#Paystub is printed after this code is ran

#Pseudocode
#Empty Lists are created to store Names, Total OT Pay for all employees, Total Reg Pay for all employees, and Total Gross Pay for all employees
#Program can handle floating point numbers for Hra and Pay Rate
#Enter information is printed in a pay stub
#Multiple employees information can be entered
#Once 'Done' is read, program prints how many employees were entered, and the Total OT, Reg, and Gross pay that was paid out for everyone entered
