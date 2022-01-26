import random
from game.player import Player


class Game:
    """
    Game class
    Responsibility of the Game is to keep track of the players names
    and number of players along with starting each round and
    asking the players if they would like to continue playing

    attributes:
        players: string- keeps track of the number of players 
        h_or_l: int - keeps trak of player's high or low guess

    methods:
        add_player: int
        start_play: None
    """
    def __init__(self):
        self.players = [self.add_player() for _ in range(int(input("How many players? ")))]
        self.h_or_l = ''
        
    def add_player(self):
        """
        Asks players' name and creates list of all players
        """
        player_name = input("What is player's name: ")
        new_player = Player(player_name,300)
        return new_player

    #Moved to __init__
    #  def num_players(self):
    #     x = 1
    #     player_count = int(input("How many players? "))
    #     while player_count > 0:
    #         player_name = input(f"What is player {x}'s name: ")
    #         new_player = Player(player_name,300)
    #         self.players.append(new_player)
    #         x +=1 
    #         player_count -= 1


    #Moved to player.py
    # def check_play(self, x, player):
    #     i = random.randint(1,13)
    #     if (self.h_or_l.lower() == 'h' and x < i) or (self.h_or_l.lower() == 'l' and x > i): 
    #         print(f"Next card was: {i}")
    #         player.score = player.score + 100
    #         print(f"{player.name}'s score is {player.score}")
    #     else: 
    #         print(f"Next card was: {i}")
    #         player.score = player.score - 75
    #         print(f"{player.name}'s score is {player.score}")


    # For in loops can be used to iterate over a list
    def start_play(self):
        """
        Starts each round
        """
        for player in self.players:
            print(f"\n{player.name}'s turn")
            player.play()

    def main(self):
        """
        Ask the player if they want to play another round
        """
        # self.num_players()
        self.start_play()
        while True: 
            again = input("Would you like to play again? [y/n]: ")
            if again.lower() == 'y':
                self.start_play()
            else:
                print("\nThanks for playing!")
                break
