
class ErrorInput(Exception):
    pass

class Calculation:

    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def title(self):
        print(f'This is a CLI Calculator')

    def add(self):
        total = self.num1 + self.num2
        print(f'Total: {total}')
    def sub(self):
        total = self.num1 - self.num2
        print(f'Total: {total}')
    def mul(self):
        total = self.num1 * self.num2
        print(f'Total: {total}')
    def div(self):
        if self.num2 == 0:
            print("Invalid, can't divide to 0")
        else:
            total = self.num1 / self.num2
            print(f'Total: {total}')

class Special(Calculation):

