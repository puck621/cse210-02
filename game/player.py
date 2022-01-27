import random

class Player: 
    """
    Player class
    The responsibility of Player is to control 
    the sequence of play and get input from the Player 

    attributes:
        name: string- name of the current player
        score: int-score for the round of play
        guess: int- player's choice of high or low

    methods:
        guess: int
        play: None
    """
    def __init__(self, name, score):
        self.score = score
        self.name = name
        self.guess: str = ""

    #def guess(self) -> str:
     #   """
      #  Ask the player for their guess.
       # """
        #return input(f"{self.name}, what is your guess? [h/l]: ")
    
    def play(self):
        """
        Play a round of the game for one player.
        """
        current_card = random.randint(1,13)
        print(f"The current card is: {current_card}")
        new_card = random.randint(1,13)
        h_or_l = input(f"{self.name}, what is your guess? [h/l]: ")
        if  h_or_l == 'h' and current_card < new_card or h_or_l == 'l' and current_card > new_card:
            print(f"{self.name}'s guess was correct!")
            self.score += 100
        else:
            print(f"{self.name}'s guess was incorrect!")
            self.score -= 75
        print(f"The next card is: {new_card}")
        print(f"{self.name}'s score is {self.score}")
        
