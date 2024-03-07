import random
import itertools
from __init__ import Counter

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
A, B, C ,D = Player("mike"), Player("John"), Player("bob"), Player("will")          #checks it
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



print(player_attributes(players))




def hand_scorer(self, player):
    # Function to score a player's hand
    seven_cards = player.cards + self.community_cards
    all_hand_combos = list(itertools.combinations(seven_cards, 5))
    list_of_all_score_possibilities = []

    for i in all_hand_combos:
        suit_list = [card[1] for card in i]
        value_list = [card[0] for card in i]
        initial_value_check = list(reversed(sorted(value_list)))

         # Check for royal flush
        if set(value_list) == {10, 11, 12, 13, 14} and len(set(suit_list)) == 1:
            score = [9, 14]  # Royal flush score
        # Check for straight flush
        elif any(initial_value_check[i] - initial_value_check[i + 4] == 4 for i in range(len(initial_value_check) - 4)) and len(set(suit_list)) == 1:
            max_value = max(initial_value_check[:5])
            score = [8, max_value]  # Straight flush score
        # Check for four of a kind
        elif any(value_list.count(value) == 4 for value in value_list):
            four_of_a_kind_value = max(set(value_list), key=value_list.count)
            score = [7, four_of_a_kind_value]  # Four of a kind score
        # Check for full house
        elif any(value_list.count(value) == 3 for value in value_list) and any(value_list.count(value) == 2 for value in value_list):
            three_of_a_kind_value = max(set(value_list), key=value_list.count)
            pair_value = min(set(value_list), key=value_list.count)
            score = [6, three_of_a_kind_value, pair_value]  # Full house score
        # Check for flush
        elif len(set(suit_list)) == 1:
            max_value = max(initial_value_check[:5])
            score = [5, max_value]  # Flush score
        # Check for straight
        elif any(initial_value_check[i] - initial_value_check[i + 4] == 4 for i in range(len(initial_value_check) - 4)):
            max_value = max(initial_value_check[:5])
            score = [4, max_value]  # Straight score
        # Check for three of a kind
        elif any(value_list.count(value) == 3 for value in value_list):
            three_of_a_kind_value = max(set(value_list), key=value_list.count)
            score = [3, three_of_a_kind_value]  # Three of a kind score
        # Check for two pair
        elif sum(value_list.count(value) == 2 for value in value_list) >= 4:
            pair_values = sorted(set(value for value in value_list if value_list.count(value) == 2), reverse=True)
            score = [2, pair_values[0], pair_values[1]]  # Two pair score
        # Check for one pair
        elif sum(value_list.count(value) == 2 for value in value_list) == 2:
            pair_value = max(set(value_list), key=value_list.count)
            score = [1, pair_value]  # One pair score
        # High card
        else:
            max_value = max(initial_value_check[:5])
            score = [0, max_value]  # High card score

        list_of_all_score_possibilities.append(score)

        # Store the best score for the player
    best_score = max(list_of_all_score_possibilities)
    player.score = best_score

def determine_winner(self):
    # Evaluate hands for each player
    for player in self.players_in_game:
        self.hand_scorer(player)
# Call determine_winner function only after all four rounds are complete
# Pass players_in_game and community_cards to the function
        
