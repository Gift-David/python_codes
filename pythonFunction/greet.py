# A script to greet a user as he enters his name
name = input("Enter your name: ").title()

def greet(name):
    print(f"Hello {name}")
greet(name)