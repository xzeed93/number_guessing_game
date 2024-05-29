import random

# Take the lower starting number input

lower_number = int(input("Enter the lower number: "))

# Take the higher starting number input

higher_number = int(input("Enter the higher number: "))

# Generate a random number between the lower and higher number

x = random.randint(lower_number, higher_number)

#Initialize the number of guesses

number_of_guesses = 0

while True:
    # Take the user's guess
    user_guess = int(input("Enter your guess: "))
    number_of_guesses += 1 # Increment the number of guesses

    if user_guess == x:
        print("Congratulations! You guessed the number in", number_of_guesses, "guesses")
        break
    elif user_guess < x:
        print("Your guess is too low")
    else:
        print("Your guess is too high")
