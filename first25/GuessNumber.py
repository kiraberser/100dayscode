from random import randint

print("Welcome to the Number Guessing Game!")
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
print("I'm thinkig of a number between 1 and 100.")
ANSWER = randint(1, 100)
print(f"Pssst, the correct answer is {ANSWER}")
choose_number = input("Choose a difficulty. Type 'easy' or 'hard': ")


def choose(live):
    if choose_number == "hard":
        live = 5
    elif choose_number == "easy":
        live = 10
    else: 
        live = 0
    return live
live = choose(0)

while live > 0: 
    guess = int(input("Make a guess: "))
    if guess > ANSWER:
        print("Too high.")
        live -= 1
        if live > 0:
            print(f"You have {live} attempts remaining to guess the number.")
    elif guess < ANSWER:
        print("Too low")
        live -= 1
        if live > 0:
            print(f"You have {live} attempts remaining to guess the number.")
    else: 
        print(f"You got it! The answer was {ANSWER}.")
        break

if live == 0:
    print(F"You lose. The answer was {ANSWER}.")
