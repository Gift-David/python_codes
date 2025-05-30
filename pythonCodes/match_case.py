
import random
secret_number = random.randint(1, 10)
guess = int(input("I'm thinking of a number between 1 and 10. Can you guess the number?"))

match guess:
    case secret_number:
        print("Congratulations, you guessed it")
    case _:
        if guess > secret_number:
            print("Your guess is a bit high. Try again!")
        elif guess < secret_number:
            print("Your guess is a bit low. Try again!")
        else:
            print("Guess not in range")
