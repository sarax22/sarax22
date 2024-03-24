from players import *
from tkinter import *
import tkinter as tk
import tkinter.simpledialog as sd
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox 
import random
import itertools
from rounds import *
from cards import *    
pot = 0

class PokerGameGUI:

    def __init__(self, master):                                          #displays the start up page with a backdrop and asks num of players/names of players
        self.master = master 
        self.master.title("My Poker Game")
        self.master.geometry("800x600")

        # Create a new frame to hold the players_frame and the start_button
        players_frame = ttk.Frame(self.master)
        players_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

        # Create a notebook widget for my tabs
        self.notebook = ttk.Notebook(players_frame)
        self.notebook.pack(fill = 'both', expand=True)

        self.round_frame = tk.Frame(self.notebook)
        self.notebook.add(self.round_frame, text = "Poker!")


        self.num_players = sd.askinteger("Number of Players", "Enter the number of players:", minvalue=2, maxvalue=6)
            
        backdrop_path = "Poker game\\backdrop_design\\xdxfdc9.jpg"
        self.backdrop_image = self.load_image(backdrop_path)
        self.backdrop_canvas = tk.Canvas(self.master, width=800, height=600)
        self.backdrop_canvas.pack()

        self.backdrop_label = tk.Label(self.backdrop_canvas, image=self.backdrop_image)
        self.backdrop_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.backdrop_canvas.create_image(0, 0, anchor=tk.NW, image=self.backdrop_image)

        self.label = tk.Label(self.master, text="My Poker Game")
        self.label.pack(padx = 20, pady = 20)

        self.starting_chips_label = tk.Label(self.master, text="Starting Chips:")
        self.starting_chips_label.pack()

        self.starting_chips_entry = tk.Entry(self.master)
        self.starting_chips_entry.pack()

        self.big_blind_label = tk.Label(self.master, text="Big Blind Amount:")
        self.big_blind_label.pack()

        self.big_blind_entry = tk.Entry(self.master)
        self.big_blind_entry.pack()

        self.small_blind_label = tk.Label(self.master, text="Small Blind Amount:")
        self.small_blind_label.pack()

        self.small_blind_entry = tk.Entry(self.master)
        self.small_blind_entry.pack()

        self.players_label = tk.Label(self.master, text="Player Names:")
        self.players_label.pack()

        self.players_entries = []
        for i in range(self.num_players):
            player_name_entry = tk.Entry(self.master)
            player_name_entry.pack()
            self.players_entries.append(player_name_entry)

        self.card_images = {}
        self.deck = None
        self.players_in_game = []
        self.community_cards = []
        self.big_blind_amount = 0
        self.pot = 0

        # Move the start_button to the new frame
        self.start_button = tk.Button(players_frame, text="Start Game", command=self.start_game)
        self.start_button.pack()


    def perform_preflop_round(self):
        self.perform_round(0)  # Assuming 0 means preflop

    def perform_flop_round(self):
        self.perform_round(3)  # Assuming 3 means flop

    def perform_turn_round(self):
        self.perform_round(1)  # Assuming 1 means turn

    def perform_river_round(self):
        self.perform_round(1)  # Assuming 1 means river

    def perform_round(self, num_community_cards):
        # Create a new deck for each round, or shuffle the existing one
        self.deck.shuffle()

        # Deal community cards
        deal_communitycards(self.deck, self.community_cards, num_community_cards)
        print(f"Community cards: {', '.join(map(str, self.community_cards))}")
        #Deal cards to players
        
        for player in self.players_in_game:
            (player, self.big_blind_amount, self.players_in_game)




    def load_image(self, path):
        image = Image.open(path)
        image = ImageTk.PhotoImage(image)
        return image

    def display_card_images(self):
        root = tk.Toplevel(self.master)  # Use Toplevel to create a new window

        # Set up a Canvas widget to display the card images
        canvas = tk.Canvas(root, width=800, height=200)
        canvas.pack()

        # Calculate the space needed for each card
        card_width = 100
        card_spacing = 10

        # Display each card image on the Canvas
        x_position = card_spacing
        for card_image_path in self.card_images.items():
            print(f"Loading image from path: {card_image_path}")
            img = Image.open(card_image_path)
            img = img.resize((card_width, 150), Image.LANCZOS)
            img = ImageTk.PhotoImage(img)
            canvas.create_image(x_position, 75, anchor=tk.W, image=img)
            x_position += card_width + card_spacing

        root.mainloop()

    def display_community_cards(self, parent_frame):
        community_cards_frame = ttk.Frame(parent_frame)
        community_cards_frame.pack(pady=10)
        for i, card in enumerate(self.community_cards):
            card_image = self.load_card_image(card)
            card_label = ttk.Label(community_cards_frame, image=card_image)
            card_label.image = card_image
            card_label.grid(row=0, column=i, padx=5)    

    def display_pot(self, parent_frame):
        pot_label = ttk.Label(parent_frame, text=f"Pot: {self.pot}")
        pot_label.pack(pady=10) 

    def display_players_info(self, parent_frame):
        players_frame = ttk.Frame(parent_frame)
        players_frame.grid(row=0, column=0, columnspan=3, sticky='nsew')
        self.round_frame.rowconfigure(0, weight=1)
        self.round_frame.columnconfigure(0, weight=1)
        self.round_frame.columnconfigure(1, weight=1)
        self.round_frame.columnconfigure(2, weight=1)

        for i, player in enumerate(self.players_in_game):
            player_frame = ttk.Frame(players_frame)
            player_frame.grid(row=i, column=0, columnspan=4, sticky='nsew', padx=5, pady=5)

            player_name_label = ttk.Label(player_frame, text=player.name)
            player_name_label.grid(row=0, column=0, padx=5, pady=5)

            player_chips_label = ttk.Label(player_frame, text=f"Chips: {player.chips}")
            player_chips_label.grid(row=0, column=1, padx=5, pady=5)

            for j, card in enumerate(player.cards):
                filename = card.get_image_filename()
                card_image = self.load_card_image(card, filename)
                card_label = ttk.Label(player_frame, image=card_image)
                card_label.image = card_image
                card_label.grid(row=1, column=j, padx=5, pady=5)

    def open_round_tab(self):
        self.round_frame.grid_remove()
        self.round_frame.grid(row=1, column=0, columnspan=3, sticky='nsew')
        self.display_pot_and_community_cards()
        self.display_players_info(self.round_frame)

    def start_game(self):
        # Create a new tab for the game
        game_frame = ttk.Frame(self.notebook)
        self.notebook.add(game_frame, text="Game")
        self.notebook.select(game_frame)

        print("Game tab created and selected.")


        # Retrieve the input values
        starting_chips = int(self.starting_chips_entry.get())
        big_blind_amount = int(self.big_blind_entry.get())
        small_blind_amount = int(self.small_blind_entry.get())

        # Retrieve player names from the entry widgets
        player_names = [entry.get() for entry in self.players_entries]

        #to initialise the game
        self.deck = StandardDeck()
        self.players_in_game = [Player(name=name) for name in player_names]
        player_attributes(self.players_in_game)
        
        # Set starting chips and cards for each player
        for player in self.players_in_game:
            player.chips = starting_chips
            player.cards = [self.deck.deal(), self.deck.deal()]

        # Start the game rounds
        self.open_round_tab()
        self.perform_preflop_round()
        self.perform_rounds()
        self.display_players_info(game_frame)
        self.display_community_cards(game_frame)
        self.display_pot(game_frame)


    def display_players_cards(self, parent_frame):
        players_frame = ttk.Frame(parent_frame)
        players_frame.grid(row=0, column=0, columnspan=3, sticky='nsew')
        self.round_frame.rowconfigure(0, weight=1)
        self.round_frame.columnconfigure(0, weight=1)
        self.round_frame.columnconfigure(1, weight=1)
        self.round_frame.columnconfigure(2, weight=1)



        for i, player in enumerate(self.players_in_game):
            player_frame = ttk.Frame(players_frame)
            player_frame.grid(row=i, column=0, columnspan=4, sticky='nsew', padx=5, pady=5)

            player_name_label = ttk.Label(player_frame, text=player.name)
            player_name_label.grid(row=0, column=0, padx=5, pady=5)

            player_chips_label = ttk.Label(player_frame, text=f"Chips: {player.chips}")
            player_chips_label.grid(row=0, column=1, padx=5, pady=5)

            for j, card in enumerate(player.cards):
                card_image = self.load_card_image(card)
                card_label = ttk.Label(player_frame, image=card_image)
                card_label.image = card_image
                card_label.grid(row=1, column=j, padx=5, pady=5)

    def display_pot_and_community_cards(self):
        # Display pot
        pot_label = tk.Label(self.round_frame, text=f"Pot: {self.pot}", font=("Arial", 16, "bold"))
        pot_label.place(relx= 0.5, rely=0.5, anchor = 'center')

        # Display community cards
        community_cards_frame = tk.Frame(self.round_frame)
        community_cards_frame.grid(row=1, column=0, columnspan=3, sticky='nsew')
        self.round_frame.columnconfigure(0, weight=1)
        self.round_frame.columnconfigure(1, weight=1)
        self.round_frame.columnconfigure(2, weight=1)

        for i, card in enumerate(self.community_cards):
            card_image = self.load_card_image(card)
            card_label = tk.Label(community_cards_frame, image=card_image)
            card_label.grid(row=0, column=i, padx=5)
    
    def load_card_image(self, card, filename):
        filename = card.get_image_filename()
        try:
            image = Image.open(filename)
            image = image.resize((100, 150), Image.LANCZOS)
            image = ImageTk.PhotoImage(image)
            return image
        except FileNotFoundError:
            print(f"Error: Image file not found for {card}")
            return None

    ##################################################################################
    def hand_calculator(self, player):
        # Function to score a player's hand
        total_cards = player.cards + self.community_cards
        all_hand_combos = list(itertools.combinations(total_cards, 5))
        list_of_all_score_possibilities = []

        for i in all_hand_combos:
            suit_list = [card.suit for card in i]
            value_list = [card.value for card in i]
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
            self.hand_calculator(player)
        winner = max(self.players_in_game, key=lambda player: player.score)

        print(f"The winner is {winner.name}. They won {self.pot} chips!")

        return pot 


    # Call determine_winner function only after all four rounds are complete
    # Pass players_in_game and community_cards to the function
            
####################################################################################################

    def perform_rounds(self):
        self.preflop_round()
        self.flop_round()
        self.turn_round()
        self.river_round()
        self.determine_winner()
         #ROUND THAT calculates and announces winner after all four rounds

    def preflop_round(self):
        self.deck.shuffle()     
        for player in self.players_in_game:
            player.cards = [self.deck.deal(), self.deck.deal()]  # Iterate over a copy of the list to allow removal
        self.pot = perform_round(self.players_in_game, self.deck, self.community_cards, 0, self.big_blind_amount)
        return self.pot
    
    def flop_round(self):
        self.pot = perform_round(self.players_in_game, self.deck, self.community_cards, 3, self.big_blind_amount)
        return self.pot


    def turn_round(self):
        self.pot = perform_round(self.players_in_game, self.deck, self.community_cards, 1, self.big_blind_amount)
        return self.pot

    def river_round(self):
        self.pot = perform_round(self.players_in_game, self.deck, self.community_cards, 1, self.big_blind_amount)
        return self.pot
  

if __name__ == "__main__":
    root = tk.Tk()
    app = PokerGameGUI(root)
    root.mainloop()