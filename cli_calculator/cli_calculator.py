
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

    try:
        num1 = float(input('1st number: '))
        num2 = float(input('2nd number: '))
        if chosen_operator == "+":
            print('Total: ' + str(add(num1, num2)) + "\n")
        else:
            raise error_input('Invalid number')

    except error_input as error:
        print(f'{error}, Character not allowed\n')
