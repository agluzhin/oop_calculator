class Calculator:

    def __init__(self, a, b) -> int:
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

    def substract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b


print('Write the first number:')
first_number = int(input())

print('Write the second number:')
second_number = int(input())

print('Chose the action needed from: +, -, *, /')
action = input()

calculation = Calculator(first_number, second_number)


def calculate(action):
    if action == '+':
        print(f"Your result: {calculation.sum()}")
    elif action == '-':
        print(f"Your result: {calculation.substract()}")
    elif action == '*':
        print(f"Your result: {calculation.multiply()}")
    elif action == '/':
        print(f"Your result: {calculation.division()}")
    else:
        print('Error...')


calculate(action)
