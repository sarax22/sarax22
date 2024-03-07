from cards import *
from players import *
from cards import deck 
pot = 0

startingchips = int(input("Starting chips? "))
bigblindamount = int(input("Big blind chips? "))
smallblindamount = int(input("Small blind chips? "))


def deal_community_cards(deck, community_cards, num_cards):
    for _ in range(num_cards):
        community_cards.append(deck.pop(0))

def perform_player_action(player, big_blind_amount, players_in_game):
    global pot 
    valid_action = False

    while not valid_action:
        action = input(f"{player.name} turn. Cards: {player.cards} Chips: {player.chips}. Pot: {pot}. Do you want to check, bet, or fold? ").lower()

        if action == "check":
            print(f"{player.name} checks.")
            valid_action = True

        elif action == "bet":
            bet_amount = input("How much do you want to bet? ")
            if bet_amount.isdigit():

                if int(bet_amount) >= big_blind_amount and player.chips >= int(bet_amount):
                    player.chips -= int(bet_amount)
                    pot += int(bet_amount)
                    print(f"{player.name} bets {bet_amount}.")
                    valid_action = True
                else:
                    print("Not enough chips to bet, try again!")
            else:
                print("That is not a number. Try again!")
        elif action == "fold":
            print(f"{player.name} has folded.")
            players_in_game.remove(player)
            valid_action = True
            if len(players_in_game) == 1:
                winner = players_in_game[0]
                print(f"The winner is {winner.name} they won {pot} chips!")
                return pot
            
        else:
            print("That is not a valid action. Try again!")

    return pot

def perform_round(players_in_game, deck, community_cards, num_community_cards, big_blind_amount):
    global pot
    deal_community_cards(deck, community_cards, num_community_cards)
    print(f"Community cards: {', '.join(map(str, community_cards))}")

    for player in players_in_game:
        perform_player_action(player, big_blind_amount, players_in_game)

        


    return pot





#ROUND 1 PREFLOP: each player dealt 2 cards X
#ask each player what action they want to take (call raise fold)
#ROUND 2 FLOP: 3 community cards are revealed X
#ask each player what action they want to take (check bet raise fold)
#ROUND 3 TURN: 1 more community card is revealed  X
#ask each player what action they want to take (check bet call raise fold)
#ROUND 4 RIVER: final community card is revealed X
#ask each player what action they want to take (check bet call raise fold)

#If there is one player left game ends - they win
#SHOWDOWN - after final betting round the players all reveal their cards !!!CANNOT CODE UNTIL CALCULATE WINNER LOGIC IS FIGURED OUT!!!
#player with the best hand wins (their cards + community cards)
#need to determine winner based on the who has the best hand + community cards combo (hand ranking system)


# Since the code for each round is identical apart from the community card handling, ive decided to try modulate it.