from art import logo, vs 
from random import randint
from game_data import data 


def randomFamous():
    return data[randint(0, len(data) -1)]

def structure(famous):
    return f"{famous['name']}, {famous['description']}, {famous['country']}"

def right(score):
    print(f"You're right, this is you score {score}")

def game():
    print(logo)
    first_famous = randomFamous()
    second_famous = randomFamous()
    game_over = False
    score = 0
    while not game_over:
        print(f"Compare A: {structure(first_famous)}")
        print(vs)
        print(f"Compare B: {structure(second_famous)}")
        choose = input("Who has more followers? Type 'A' or 'B': ").lower()
        is_correct = (choose == "a" and first_famous['follower_count'] > second_famous['follower_count']) or (choose == "b" and second_famous['follower_count'] > first_famous['follower_count'])
        score = score + 1 if is_correct else score
        if is_correct:
            right(score)
            first_famous = second_famous
            second_famous = randomFamous()
        else:
            print(f"You lose, final score: {score}")
            game_over = True
game()
