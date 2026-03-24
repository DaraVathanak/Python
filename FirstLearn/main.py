import math
name = input('What is your name?: ')
age = int(input('How old are you?: '))
price1 = float(input('Insert your price: '))
price2 = float(input('Insert your price: '))

age = age + 1
total_price = price1 + price2

print(f'Hello {name}')
print(f'You are {age} year old')
print(f'The Total Price: ${total_price}')

length = float(input('Enter Length: '))
width = float(input('Enter Width: '))

Area = length*width

print(Area)

radius = float(input('Enter the radius of a circle: '))

circumference = 2*math.pi*radius

print(f'The circumference is: {round(circumference,2)}')
