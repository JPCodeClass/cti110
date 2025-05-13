#Jackson Porter
#3/16/2025
#P2HW1
#This program will take user input for a trip, and return those values and the remaining budget nicley formatted


print('This program calculated and displays travel expenses')
initial_budget = float(input('Enter Budget: '))
print()
destination = input('Enter your travel destination: ')
print()
gas = float(input('How much do you think you will spend on gas?'))
print()
hotel = float(input('Approximatley, how much will you need for accomodation/hotel?'))
print()
food = float(input('Last, how much will you need for food?'))

#Math
expenses = gas + hotel + food
remaining_balance = initial_budget - expenses
#

print()
print('----------Travel Expenses----------')
print(f'Locaiton:            {destination}')
print(f'Initial Budget:      ${initial_budget:.2f}')
print(f'Fuel:                ${gas:.2f}')
print(f'Accomodations:       ${hotel:.2f}')
print(f'Food:                ${food:.2f}')
print('-----------------------------------')
print(f'Remaining Balance:   ${remaining_balance:.2f}')
