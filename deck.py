from cards import *
import random

#the Deck of cards, can be built by user input and used to play any cards game

class Deck :
    def __init__(self,start, end, number_of_suits):
        self.number_of_suits = number_of_suits
        self.value_start = start
        self.value_end = end
        self.random_suit = random.sample((fullsuits), self.number_of_suits)
        self.cards = []
        self.hand = []
        for face in range(self.value_start, self.value_end):
            for suit in self.random_suit:
                self.cards.append(Cards(fullfaces[face],suit))

    #function to shuffle the deck
    def shuffle(self):
        random.shuffle(self.cards)

    #function to add random a card that the deck doesn't have yet
    def addrd_card(self):
        new_card = Cards(random.choice(fullfaces), random.choice(fullsuits))
        if new_card in self.cards :
            pass
        else :
            self.cards.append(new_card)
            return self.cards

    #function to draw a card from a deck
    def draw(self):
        card = self.cards.pop()
        self.hand.append(card)
        return card

    def __str__(self):
        return self.cards

    def __repr__(self):
        return 'The deck of {!r} card(s), {!r} suit(s)'.format((self.value_start-self.value_end), self.number_of_suits)


#The playboard of freecell game, consits a Deck with 52 cards.

class deck_freecell (object):
    def __init__(self, the_empty = '--'):
        self.deck = Deck (1,14,4)
        self.deck.shuffle()
        self.foundations = []
        self.freecells = []
        self.cascade = []
        self.empty = the_empty

        i = 0
        while (i < 1):
            self.foundations.append([self.empty] * 4)
            i += 1

        while (i < 2):
            self.freecells.append([self.empty] * 4)
            i += 1

        #draw the card from deck and distribute it to the cascade
        for card in self.deck.cards:
            self.cascade.append(card)

        #split the cards into columns sets
        self.cascade = [self.cascade[x:x + 8] for x in range(0, len(self.cascade), 8)]

        #fill up the empty spaces in the cascade with the empty string'--'
        for row_idx, row in enumerate(self.cascade) :
            while len(row) < 8:
                self.cascade[row_idx].append(self.empty)

    #return the string of the freecell playboard
    def __str__(self):
        cascade_string = ''
        foundations_string = ''
        freecells_string = ''

        #add empty strings in the foundation area
        for item1 in self.foundations:
            for i in item1:
                foundations_string += str(i) + '\t'

        #add emptry strings in the freecells area
        for item2 in self.freecells:
            for i in item2:
             freecells_string += str(i) + '\t'

        #print out the cascade playboard(reference:Gavin's Chessboard, w10 lecture)
        for r in self.cascade:
            for item in r:
                cascade_string += str(item) + '\t'
            cascade_string.strip('\t')
            cascade_string += '\n'
        return '[' + freecells_string + ']' + '\t' + '[' + foundations_string + ']' + '\n' + cascade_string

    #function to take a card out of a column in the cascade
    def get_card(self,c):
        if c < 8:
            for r in range(1,30):
                if not self.is_empty(-r,c):
                    card = self.cascade[-r][c]
                    self.cascade[-r][c] = self.empty
                    break
            return card
        else:
            return print('the card does not exist')

    #function to add any card to the end of a column in the cascade
    def add_card(self,the_card,c):
        if c < 8 :
            for r in range(1,30):
                if self.cascade[-r][c] != '--':
                    self.cascade.append(['--'] * 8)
                    self.cascade[-r][c] = the_card
                    break
                elif self.cascade[-r-1][c] != '--':
                        self.cascade[-r][c] = the_card
                        break
                elif self.cascade[r-1][c] == self.empty:
                    self.cascade[r-1][c] = the_card
                    break
        else:
            print("Column " + str(c+1) + " does not exist.")

    #function to check if a place in the cascade is empty
    def is_empty(self,r,c):
        if self.cascade[r][c] == self.empty:
            return self.cascade[r][c] == self.empty










