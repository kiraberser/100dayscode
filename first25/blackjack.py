import random
from art import logo

def add(n1, n2):
  return n1 + n2 

def random1():
  return random.randint(1, 25)


def blackjack():

  should_continue = True
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  while should_continue:
    question = input("Do you want to play a game of Blackjack? type 'y' or 'n': ")
    if question == "n":
      should_continue = False
    elif question == "y":
      print(logo)
      card1 = cards[random1()]
      card2 = cards[random1()]
      sum = add(card1, card2)
      card3 = cards[random1()]
      first = print(f"Your cards: [{card1}, {card2}], current score: {sum}")
      second = print(f"Computer's first card: {card3}")
      question = input("Type 'y' to get another card, type 'n' to pass: ")
      if question == "y":
        cards4 = cards[random1()]
        cards5 = cards[random1()]
        sum1 = sum + cards4
        first = print(f"Your cards: [{card1}, {card2}, {cards4}] current score: {sum1}")
        second = print(f"Computer's first card: {card3}")
        if sum1 > 21:
          print (f"Your final hand: [{card1}, {card2}, {cards4}] current score: {sum1}")
          sum1 = sum + cards5
          print(f"Computer's final hand: [{card3}, {cards5}], final score: {sum1}")
          
blackjack()
    