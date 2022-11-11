from card import Card
from random import shuffle
class Deck:
    def __init__(self):
        suits=['♣','♦','♥','♠']
        Ranks=['2','3','4','5','6','7','8','9','10','jak','queen','king','ace']
        cardes=[]
        for i in range(4):
            for j in range(13):
                c=Card(i,j)
                cardes.append(c)
        self.cards=cardes
    def __str__(self):
        for i in self.cards:
            print(i)
    def __len__(self):
        return len(self.cards)   
    def add_card(self,card):
        self.cards.append(card)
    def pop_card(self):
        if len(self.cards):
            return self.cards.pop(0)
    def shuffle(self):
        shuffle(self.cards)
    
        
