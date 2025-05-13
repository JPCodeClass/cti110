#Jackson Porter
#3/2/2025
#P1HW2
#Coding a travel budget guide

#Pseudocode
#Ask the user to input their budget and location for a trip
#Then enter the cost of gas, hotel, and food
#Take the starting balance and subtract the food, hotel, and gas to give them the remaining budget

print('This program calsulates and displays travel expenses')
budget = float(input('Enter Budget: '))
destination = input('Enter your travel destination: ')
gas = float(input('How much do you think you will spend on gas? '))
hotel = float(input('Approximately, how much will you need for accomodation/hotel? '))
food = float(input('Last, how much do you need for food? '))
print()



print('-------Travel Expenses-------')
print('Location:', destination)
print('Initial Budget:', '$'f'{budget:.2f}')

print('Fuel:', '$'f'{gas:.2f}', '\nAccomodation:', '$'f'{hotel:.2f}', '\nFood:', '$'f'{food:.2f}')

print('Remaining Balance:', budget - gas - hotel - food)

