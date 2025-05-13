#Jackson Porter
#3/23/2025
#P3LAB
#Coding a program to return change to a user using // and if-ifelse

dollar_input = float(input('Enter the amount of money as a float: $'))
dollar_integer = int(dollar_input * 100)

#Change Math
dollars = 100
quarters = 25
dimes = 10
nickles = 5
pennies = 1

#If Amount Starts at 0
if dollar_integer == 0:
    print('No Change')

#Dollars
dollars_needed = dollar_integer // dollars
dollar_integer = dollar_integer - (dollars_needed * 100)

#Quarters
quarters_needed = dollar_integer // quarters
dollar_integer = dollar_integer - (quarters_needed * 25)

#Dimes
dimes_needed = dollar_integer // dimes
dollar_integer = dollar_integer - (dimes_needed * 10)

#Nickles
nickles_needed = dollar_integer // nickles
dollar_integer = dollar_integer - (nickles_needed * 5)

#Pennies
pennies_needed = dollar_integer 




#Printed Change
if dollars_needed == 1:
    print(dollars_needed, 'Dollar')
elif dollars_needed >= 2:
    print(dollars_needed, 'Dollars')


if quarters_needed == 1:
    print(quarters_needed, 'Quarter')
elif quarters_needed >= 2:
    print(quarters_needed, 'Quarters')
    

if dimes_needed == 1:
    print(dimes_needed, 'Dime')
elif dimes_needed >= 2:
    print(dimes_needed, 'Dimes')


if nickles_needed ==1:
    print(nickles_needed, 'Nickle')
elif nickles_needed >= 2:
    print(nickles_needed, 'Nickles')


if pennies_needed ==1:
    print(pennies_needed, 'Penny')
elif pennies_needed >= 2:
    print(pennies_needed, 'Pennies')



