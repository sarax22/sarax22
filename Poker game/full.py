import random
import tkinter as tk
import tkinter.simpledialog as sd
from PIL import Image, ImageTk
from tkinter import messagebox 
import random

class Card(object):                                      #creating a class for the object 'card' and assigning each card its value and suit to create a deck later on
     def __init__(self, value, suit):
         self.value = value
         self.suit = suit
            
     def __repr__(self):                                                                   #using repr to represent cards as actual suits and values not just numbers
        value_name = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]
        suit_name = ["hearts","diamonds", "clubs","spades"]
        return f"{value_name[self.value]} of {suit_name[self.suit]}"                                           #returns each card as actual cards aka ace of diamonds

     def get_image_filename(self):
         return f'D:\Poker Prototypes\card_images{self.value_name[self.value]}_of_{self.suit_name[self.suit]}.png'
     


class StandardDeck(list):
    def __init__(self):
        super().__init__()                           #returns temp object of standarddeck class with the same methods (inheritance)
        suits = list(range(4))                       #4 different suits, i
        values = list(range(13))                     #13 different values, j
        for i in values:
            for j in suits:
                self.append(Card(i, j))                         #will give 4x13 cards = 52 (standard deck)
            

    def shuffle(self):
        random.shuffle(self)                                    #uses the library random to shuffle deck of cards
        print("deck has been shuffled")

    def deal(self, player):                                     #easy method to deal cards
        player.cards.append(self.pop(0))                        #pops one card off of the deck stack and print it out 

def deal_communitycards(deck, communitycards, num_cards):       #function to deal community cards
    for _ in range(num_cards):
        communitycards.append(deck.pop(0))




deck = StandardDeck()
print(deck)



def deal_communitycards(deck, communitycards, num_cards):       #function to deal community cards from cards i put in here for now
    for _ in range(num_cards):
        communitycards.append(deck.pop(0))

startingchips = int(input("Starting chips? "))
bigblindamount = int(input("Big blind chips? "))
smallblindamount = int(input("Small blind chips? "))


def preflop_round(self, players_in_game): #this is the logic behind preflop round only
    pot = 0
    for player in players_in_game:  
        print(player.name + "turn.")
        print("Chips" + player.chips)
        print("Current pot: " + pot)

    valid_action = False
    while valid_action != False:
        action = input("Do you want to call, raise or fold?").lower()

        if action == "call":
            if player == players_in_game[0]:
                callamount = bigblindamount
            else:
                callamount = smallblindamount
            if player.chips >= callamount:
                player.chips -= callamount               #updates players chips
                pot += callamount                        #updates pot
                print(player.name + "has called.")
                valid_action = True                      #checks if the action is valid and updates valid_action to be true if it is
            else:
                print("Not enough chips to call. Try again.")

        elif action == "raise":
            raiseamount = int(input("how much do you want to raise by? "))
            if player.chips >= raiseamount:
                player.chips -= raiseamount
                pot += raiseamount
                print(player.name + "Has raised by" + raiseamount)
                valid_action = True
            else:
                print("Not enough chips to raise. Try again.")

        elif action == "fold":
            print(player.name + "has folded")
            valid_action = True                          #valid_action = true makes sure that if the action is valid, it wont carry on looping and will end there for that player

        else:
            print("That is not a valid action. Try again!")

def flop_round(players_in_game, communitycards):
    deal_communitycards(deck, communitycards, 3)
    print("community cards: ", " , ".join(map(str, communitycards)))

    for player in players_in_game:
        print(player.name + "turn.")
        print("Chips: " + player.chips)

        valid_action = False
        while valid_action != False:

            action = input("Do you want to check, bet or fold?").lower()
            if action == "check":
                print(f"{player.name} checks.")
                valid_action = True

            elif action == "bet":
                betamount = int(input("How much do you want to bet? "))
                if betamount >= bigblindamount and player.chips>= betamount:
                    player.chips -= betamount
                    pot += betamount
                    print(f"{player.name} bets {betamount}.")
                    valid_action = True
                else:
                    print("Not enough chips to bet, try again!")
            
            elif action == "fold":
                print(player.name + "has folded.")
                valid_action = True
            else:
                print("That is not a valid action. Try again!")

def turn_round(players_in_game, communitycards):                  #repeat for turn round
    deal_communitycards(deck, communitycards, 1)                  #deal another community card
    print("community cards: ", " , ".join(map(str, communitycards)))            #reveal the community cards

    for player in players_in_game:
        print(player.name + "turn.")
        print("Chips: " + player.chips)

        valid_action = False
        while valid_action != False:
            action = print("Do you want to check, bet or fold?").lower()

            if action == "check":
                print(player.name + " checks.")
                valid_action = True

            elif action == "bet":
                betamount = int(input("How much do you want to bet"))
                if betamount >= bigblindamount and player.chips >= betamount:            #checks that they bet atleast bigblind amount which is minimum
                    player.chips -= betamount
                    pot += betamount
                    print(f"{player.name} bets {betamount}.")
                    valid_action = True
                else:
                    print("Not enough chips to bet, try again!")
            elif action == "fold":
                print(f"{player.name} has folded.")
                valid_action = True
            else:
                print("That is not a valid action, try again!")

def river_round(players_in_game, deck, communitycards):      #repeat for river round 
    deal_communitycards(deck, communitycards, 1)             #deal final community card

    print("Community cards: ", " , ".join(map(str, communitycards))) #reveal final community card

    for player in players_in_game: 
        print(f"{player.name} turn.")
        print(f"Chips: {player.chips}")


        valid_action = False
        while valid_action != False:
            action = input("Do you want to check, bet or fold?").lower()

            if action == "check":
                print(player.name + " checks.")
                valid_action = True

            elif action == "bet":
                betamount = int(input("How much do you want to bet"))
                if betamount >= bigblindamount and player.chips >= betamount:
                    player.chips -= betamount
                    pot += betamount
                    print(f"{player.name} bets {betamount}.")
                    valid_action = True
                else:
                    print("Not enough chips to bet, try again!")
            elif action == "fold":
                print(f"{player.name} has folded.")
                valid_action = True
            else:
                print("That is not a valid action, try again!")



class Player(object):
    def __init__(self, name=None):
        self.name = name
        self.chips = 0
        self.stake = 0
        self.stake_gap = 0
        self.cards = []           #needs to be alist so that we can append it
        self.score = []
        self.fold = False
        self.ready = False
        self.all_in = False
        self.win = False
        self.list_of_special_attributes = []
A, B, C ,D = Player("mike"), Player("John"), Player("bob"), Player("will")
players = [A, B, C, D]



player1 = Player("Mike")


def player_attributes(players_in_game):
    address_assignment = 0
    dealer = players_in_game[address_assignment]
    dealer.list_of_special_attributes.append("dealer")
    address_assignment += 1
    address_assignment = address_assignment % len(players_in_game)
    small_blind = players_in_game[address_assignment]
    small_blind.list_of_special_attributes.append("small blind")
    address_assignment += 1
    address_assignment %= len(players_in_game)
    big_blind = players_in_game[address_assignment]
    big_blind.list_of_special_attributes.append("big blind")
    address_assignment += 1
    address_assignment %= len(players_in_game)
    first_act = players_in_game[address_assignment]
    first_act.list_of_special_attributes.append("first actor")
    players_in_game.append(players_in_game.pop(0))

player_attributes(players)


 if __name__ == "__main__":
    root = tk.Tk()
    app = PokerGameGUI(root)
    root.mainloop()
