num1 = int(input('enter the first number '))
num2 = int(input('enter the second number '))
oper = input('enter the operator ')

if oper == '+':
    print(num1+num2)
elif oper == "-":
    print(num1-num2)
elif oper == "*":
    print(num1*num2)
elif oper == "/":
    print(round(num1/num2))
    print(num1 % num2)
else:
    print('What you typed isn\'t a basic operator')
