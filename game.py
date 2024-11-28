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
    
    def turns_comparison(self,player_turn):
        computer_turn = self.computer_turn()
        if(computer_turn == player_turn):
            return('Draw!',computer_turn)
        elif(computer_turn == self.variants[player_turn]):
            self.player_score += 1
            return('Player wins!',computer_turn)
        else:
            self.computer_score +=1
            return('Computer wins!',computer_turn)
    
    def score_calc(self):
        return [self.computer_score,self.player_score]
    
    def run_game(self,user_value):
        result = self.turns_comparison(user_value)
        scores = self.score_calc()
        return result,scores
    
    def find_winner(self):
        if(self.computer_score > self.player_score):
            return f'The winner is Computer with score {self.computer_score}!'
        elif(self.computer_score == self.player_score):
            return f'Draw! Computer and Player have the same score : {self.computer_score}'
        else:
            return f'The winner is Player with score {self.player_score}'