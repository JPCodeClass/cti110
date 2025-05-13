#Jackson Porter
#4/6/2025
#P4LAB2
#This program asks users to input a number and it prints a 1-12 multiplication table for the user, it is also repeatable with new input

program_start = 0
user_input_int = int(input('Enter an integer: '))
print()


while program_start == 0:
    if user_input_int <= -1:
        print('This program does not handle negative numbers')
        rerun = input('Would you like to run the program again? ')
        if 'yes' in rerun:
            user_input_int = int(input('Enter an integer: '))
        elif 'no' in rerun:
            print('Exiting program...')
            exit()
            break
    else:
        for i in range(1, 13):
            print(f'{user_input_int} * {i} = {user_input_int * i}')
        rerun = input('Would you like to run the program again? ')
        if 'yes' in rerun:
            user_input_int = int(input('Enter an integer: '))
        elif 'no' in rerun:
            print('Exiting program...')
            exit()
                                 
                
                
            

