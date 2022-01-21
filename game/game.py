import random
from game.player import Player


class Game:
    # This is a slightly more 'pythonic' way of doing num_players
    def __init__(self):
        self.players = [self.add_player() for i in range(int(input("How many players? ")))]
        
    def add_player(self):
        player_name = input("What is player's name: ")
        new_player = Player(player_name,300)
        return new_player

    # End Emmett's Changes

    def num_players(self):
        x = 1
        player_count = int(input("How many players? "))
        while player_count > 0:
            player_name = input(f"What is player {x}'s name: ")
            new_player = Player(player_name,300)
            self.players.append(new_player)
            x +=1 
            player_count -= 1




    def check_play(self, x, y):
        i = random.randint(1,13)
        if self.h_or_l.lower() == 'h':
            if x < i:
                print(f"Next card was: {i}")
                self.players[y].score = self.players[y].score + 100
                print(f"{self.players[y].name}'s score is {self.players[y].score}")
            else: 
                print(f"Next card was: {i}")
                self.players[y].score = self.players[y].score - 75
                print(f"{self.players[y].name}'s score is {self.players[y].score}")
        elif self.h_or_l.lower() == 'l':
            if x > i:
                print(f"Next card was: {i}")
                self.players[y].score = self.players[y].score + 100
                print(f"{self.players[y].name}'s score is {self.players[y].score}")
            else:
                print(f"Next card was: {i}")
                self.players[y].score = self.players[y].score - 75
                print(f"{self.players[y].name}'s score is {self.players[y].score}")

    def start_play(self):
        y = 0
        for count in self.players:
            print(f"\n{self.players[y].name}'s turn")
            x = random.randint(1,13)
            print(f"The card is: {x}")
            self.h_or_l = input("Higher or Lower [h/l]: ")
            self.check_play(x, y)
            y+=1

    def main(self):
        self.num_players()
        self.start_play()
        while True: 
            again = input("Would you like to play again? [y/n]: ")
            if again.lower() == 'y':
                self.start_play()
            else:
                print("\nThanks for playing!")
                break
