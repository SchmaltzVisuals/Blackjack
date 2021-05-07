import random
#Selection of cards to choose from
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#user cards is the players card stack
user_cards = []
computer_cards = []


# deal 2 cards to the player & the computer. 
# Also checks for a case of dealing 2 11s
# add the cards together to get the totals, return

def initial_deal():
  user_total = 0
  computer_total = 0
  card = random.choice(cards)
  
  if len(user_cards) < 2:
    user_cards.append(card)
    initial_deal()
    if user_cards[0] == 11 and user_cards[1] == 11:
      user_cards[1] = 1
  for value in user_cards:
    user_total += value

  if len(computer_cards) < 2:
    computer_cards.append(card)
    initial_deal()
    if computer_cards[0] == 11 and computer_cards[1] == 11:
      computer_cards[1] = 1
  for value in computer_cards:
    computer_total += value

  return user_total, computer_total
  
# initiate the funtion
initial_deal()  
user_total, computer_total = initial_deal()

print(f"The computers first card is: {computer_cards[:1]}")

#called if the user replies with 'hit'
def user_deal_card(user_total):
  card = random.choice(cards)
  if card == 11:
    card = 1
    user_cards.append(card)
    user_total += card
    return user_total
  else:
    user_cards.append(card)
    user_total += card
    return user_total

#this function is exclusive the the computer and runs
#automatically if the computer has less than 17 totals
#if the computer gets two 11s, the 2nd will be replaced
#with a 1. Then appends the card to the total.


def computer_deal_card(computer_total):
  card = random.choice(cards)
  if card == 11 and computer_total < 17:
    card = 1
    computer_cards.append(card)
    print(card)
    computer_total += card
  else:
    computer_cards.append(card)
    computer_total += card
  return computer_total

#calls the above function
while computer_total < 17:
  computer_total = computer_deal_card(computer_total)


#could be more efficient but a simple if/elif function
#to check who won or if it was a draw 

def check_winner(user_total, computer_total):
  if computer_total == 21 and user_total != 21:
    print("Blackjack for the bot!")
  elif user_total == 21 and computer_total != 21:
    print("Blackjack for the user!")
  elif user_total < 21 and user_total > computer_total:
    print("The user wins!")
  elif computer_total < 21 and computer_total > user_total:
    print("The bot wins!")
  elif user_total < 21 and computer_total > 21:
    print("The user wins!")
  elif computer_total < 21 and user_total > 21:
    print("The bot wins!")
  else:
    print("Draw!")
  print(f"The computer's cards were: {computer_cards}, giving them a total of: {computer_total}")
  exit()

print(f"Your two cards are: {user_cards}")

#ask the user if they would like to add another card
#or if they want to take a chance with what they have.

def user_choice(user_total):
  while user_total < 21:
    decision = input("Would you like to hit or stay?\n")
    if decision == 'hit':
      user_total = user_deal_card(user_total) 
      print(f"Your total value is: {user_total}")
    else:
      check_winner(user_total, computer_total)
  if user_total > 21:
    check_winner(user_total, computer_total)

user_choice(user_total)

