# A script that uses the calculator module to do arithmetic operations
import calculator

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

addition = calculator.add(num1, num2)
subtraction = calculator.subtract(num1, num2)
division = calculator.divide(num1, num2)
multiplication = calculator.multiply(num1, num2)

print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} / {num2} = {division}")
print(f"{num1} * {num2} = {multiplication}")