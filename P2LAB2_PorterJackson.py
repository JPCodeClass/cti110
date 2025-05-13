#Jackson Porter
#3/9/2025
#P2LAB2
#Dictionary input and Display output from User

cars = {
    'Camaro': 18.21,
    'Prius': 52.36,
    'Model S': 110,
    'Silverado': 26,
}

keys = cars.keys()
print(keys)
car_name  = input('Enter a vehcile to see its mpg:')
print('The', car_name, 'gets', cars[car_name], 'mpg')
miles_driven = int(input(f'How many miles will you drive the {car_name}? '))

gallons_needed = miles_driven / cars[car_name]

print(f'{gallons_needed:.2f}', 'gallons(s) of gas are needed to drive the', car_name, miles_driven, 'miles.')

