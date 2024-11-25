import random

class Game():
    def __init__(self):
        self.variants = {
            'Paper':'Rock',
            'Scissors':'Paper',
            'Rock':'Scissors',
        }
        self.turns = ['Rock','Paper','Scissors']
        self.player_score = 0
        self.computer_score = 0
    
    def computer_turn(self):
        turn = self.turns[random.randint(0,2)]
        return turn
    
    def enter_turn(self):
        player_turn = (input('Enter your turn please: ')).strip().title()
        if(player_turn in self.turns or player_turn == 'End'):
            return player_turn
    
    def turns_comparison(self,player_turn):
        computer_turn = self.computer_turn()
        if(computer_turn == player_turn):
            return('Draw!')
        elif(computer_turn == self.variants[player_turn]):
            return('Player wins!')
        else:
            return('Computer wins!')
    
    def score_calc(self,winner):
        if(winner.split()[0] == 'Player'):
            self.player_score += 1
        elif(winner.split()[0] == 'Computer'):
            self.computer_score +=1
    
    def run_game(self):
        alive = True
        while alive:
            player_turn = self.enter_turn()
            if player_turn == 'End':
                if(self.player_score > self.computer_score):
                    print(f'The winner is Player with score {self.player_score}!')
                else:
                    print(f'The winner is Computer with score {self.computer_score}!')
                alive = False
            else:
                result = self.turns_comparison(player_turn.title())
                print(result)
                self.score_calc(result)