import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
random_number = random.randint(1, 100)
print(f"The right number is {random_number}")
defficulty_level = input("Choose a difficulty level ('easy' or 'hard'):")

def guess_number(difficulty):
    if difficulty == "easy":
        lives = 10
    elif difficulty == "hard":
        lives = 5
    else:
        print("You must select any difficulty")
        return

    while lives > 0:
        print(f"You have {lives} attemps remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if guess > random_number:
            print("Too high.\nGuess again.")
        elif guess < random_number:
            print("Too low.\nGuess again.")

        else:
            print(f"Congratulations! You guessed the number {random_number}")
            break
        lives -= 1
    
    if lives == 0:
        print(f"Sorry, you've run out of attemps. The correct number was {random_number}.")
guess_number(defficulty_level)
