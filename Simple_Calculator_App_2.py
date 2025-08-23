
print('Welcom to Python Calculator App 2')

print('--------------------------------------')

num1=float(input('Enter the First Number: '))
num2=float(input('Enter the Second Number: '))

Operator=input('Enter the Operator (+, -, /, *, %): ')

if Operator== '+':
     print('The Result is: '+str(num1+num2))
    
elif Operator== '-':
     print('The Result is: '+str(num1-num2))
    
elif Operator== '/':
    if num2!=0
     print('The Result is: '+str(num1/num2))
    else:
        print("Can't Division by Zero!!")
elif Operator== '*':
     print('The Result is: '+str(num1*num2))
    
elif Operator== '%':
     print('The Result is: '+str(num1%num2))
     
else :
    print('Sorry There is somthing wrong!!')