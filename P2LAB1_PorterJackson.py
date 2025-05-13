#Jackson Porter
#3/9/2025
#P2LAB1
#The program asks the user to enter the radius of a cirlce, and the program will return the Diameter, Circumference, and Area

cir_radius =  float(input('What is the radius of the circle? '))
print()

#Math
pi = 3.14
cir_diameter = 2 * cir_radius
cir_circumference = 2 * pi * cir_radius
cir_area = pi * (cir_radius ** 2)
#

print(f'The diameter of the circle is {cir_diameter:.1f}\n')
print(f'The circumference of the circle is {cir_circumference:.2f}\n')
print(f'The area of the cicle is {cir_area:.3f}')
