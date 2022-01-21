import random
from game.player import Player


class Game:

    players = []
    h_or_l = ''

    def num_players():
        x = 1
        player_count = int(input("How many players? "))
        while player_count > 0:
            player_name = input(f"What is player {x}'s name: ")
            new_player = Player(player_name,300)
            Game.players.append(new_player)
            x +=1 
            player_count -= 1

    def check_play(x, y):
        i = random.randint(1,13)
        if Game.h_or_l.lower() == 'h':
            if x < i:
                print(f"Next card was: {i}")
                Game.players[y].score = Game.players[y].score + 100
                print(f"{Game.players[y].name}'s score is {Game.players[y].score}")
            else: 
                print(f"Next card was: {i}")
                Game.players[y].score = Game.players[y].score - 75
                print(f"{Game.players[y].name}'s score is {Game.players[y].score}")
        elif Game.h_or_l.lower() == 'l':
            if x > i:
                print(f"Next card was: {i}")
                Game.players[y].score = Game.players[y].score + 100
                print(f"{Game.players[y].name}'s score is {Game.players[y].score}")
            else:
                print(f"Next card was: {i}")
                Game.players[y].score = Game.players[y].score - 75
                print(f"{Game.players[y].name}'s score is {Game.players[y].score}")

    def start_play():
        y = 0
        for count in Game.players:
            print(f"\n{Game.players[y].name}'s turn")
            x = random.randint(1,13)
            print(f"The card is: {x}")
            Game.h_or_l = input("Higher or Lower [h/l]: ")
            Game.check_play(x, y)
            y+=1

    def main():
        Game.num_players()
        Game.start_play()
        while True: 
            again = input("Would you like to play again? [y/n]: ")
            if again.lower() == 'y':
                Game.start_play()
            else:
                print("\nThanks for playing!")
                break
