import random
from PIL import Image
def deal(self):                                     #easy method to deal cards
    return self.pop(0)                                      #pops one card off of the deck stack and print it out 


def deal_communitycards(deck, communitycards, num_cards):       #function to deal community cards
    for _ in range(num_cards):
        communitycards.append(deck.pop(0))


class Card(object):                                      #creating a class for the object 'card' and assigning each card its value and suit to create a deck later on
     def __init__(self, value, suit):
         self.value = value
         self.suit = suit
            
     def __repr__(self):                                                                   #using repr to represent cards as actual suits and values not just numbers
        value_name = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
        suit_name = ["hearts","diamonds", "clubs","spades"]
        return f"{value_name[self.value]} of {suit_name[self.suit]}"                                           #returns each card as actual cards aka ace of diamonds

     def get_image_filename(self):
         value_name = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]
         suit_name = ["hearts","diamonds", "clubs","spades"]
         return f'Poker game\\card_images\\{value_name[self.value]}_of_{suit_name[self.suit]}.png'



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


    def deal(self):                                     #easy method to deal cards
        return self.pop(0)

deck = StandardDeck()
print(deck)

# Assuming you have a card object
test_card = Card(2, 0)  # For example, 2 of hearts

# Get the image filename
filename = test_card.get_image_filename()

# Load the image using PIL
image = Image.open(filename)

# Display the image
image.show()