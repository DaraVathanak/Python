Operator = input('Enter an operator(+ - * /): ')
num1 = float(input('Enter the first number: '))
num2 = float(input('Enter the second number: '))

if Operator=="+":
    result = num1+num2
    print(result)
elif Operator=="-":
    result = num1-num2
    print(result)
elif Operator=="*":
    result = num1*num2
    print(result)
elif Operator=="/":
    result = num1/num2
    print(result)
else:
    print(f'{Operator} is not right of operator')
