
def add(x,y):
    return x+y

def sub(x,y):
    return  x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

def operate():
    operators = {"+","-","/","*"}
    while True:
        operator = input('Operator: ')
        if operator in operators:
            return operator
        else:
            print('Invalid operator')

class error_input(Exception):
    pass

while True:

    print('=== This is a CLI Calculator 🔢 ===\n Choose "+,-,/,*"')
    chosen_operator = operate()

    while True:
        try:
            num1 = float(input('1st number: '))
            num2 = float(input('2nd number: '))
            break

        except ValueError:
            print('Character not allowed\n')

    if chosen_operator == "+":
        total = add(num1, num2)
    elif chosen_operator == "-":
        total = sub(num1, num2)
    elif chosen_operator == "*":
        total = mul(num1, num2)
    elif chosen_operator == "/":
        if num2 == 0:
            raise error_input("It is not possible")
        total = div(num1, num2)

    print(f'Total: {total:.2f}\n')
    if input('Do you want to try again? "y" for yes or any key to quit: ').lower().strip() == 'y':
        continue
    else:
        break

