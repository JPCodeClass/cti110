#Jackson Porter
#4/20/2025
#P5LAB
#Use of loops, fuctions, and imports to emulate a self checkout machine to return change to the user
import random
def disperse_change(amount):
    dollar_integer = int(round(amount * 100))

#Change Math
    dollars = 100
    quarters = 25
    dimes = 10
    nickles = 5
    pennies = 1


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
        print(nickles_needed, 'Nickel')
    elif nickles_needed >= 2:
        print(nickles_needed, 'Nickels')


    if pennies_needed ==1:
        print(pennies_needed, 'Penny')
    elif pennies_needed >= 2:
        print(pennies_needed, 'Pennies')

#Random Generation of Amount Owed
def main():
    money_owed = round(random.uniform(0.01, 100.00), 2)
    owed_in_cents = int(money_owed * 100)
    print(f"You owe ${owed_in_cents // 100}.{owed_in_cents % 100:02d}")
    
#Ask User for Input
    money_payed = float(input("How much cash will you put in the self-checkout?"))
    payed_in_cents = int(money_payed * 100)

#Print Change for the User
    while payed_in_cents > owed_in_cents:    
        change_cents = payed_in_cents - owed_in_cents
        print(f"Change is ${change_cents // 100}.{change_cents % 100:02d}")

        disperse_change(change_cents / 100)
        break

main()
                    

