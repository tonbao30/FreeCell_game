# the card face in the order lowest to highest
fullfaces = ['Joker','A', '2', '3', '4', '5', '6', '7', '8', '9', 'X', 'J', 'Q', 'K']
#suits of the cards
fullsuits = ['C', 'D', 'H', 'S']

class Cards:
    def __init__(self, face, suit):
        self.face = face
        self.suit = suit
        #return TRUE if the card face is either Heart 'H' or Diamond 'D',
        #return FALSE if the card face is Club 'C' or Spade 'S'
        self.color = suit in 'HD'

    #define if a card equal to other card
    def __eq__(self, other):
      if isinstance(other, Cards):
         return self.face == other.face and self.suit == other.suit
      elif isinstance(other, str):
         return str(self) == other

    #define the if a card have a greater rank (face) than other.
    def __gt__(self, other):
        return fullfaces.index(str(self.face)) > fullfaces.index(str(other.face))

    #define a card format that will be append to the deck
    def __repr__(self):
      return 'Card({!r}, {!r})'.format(self.face, self.suit)

    # define a card format that will be show to user
    def __str__(self):
      return str(self.face) +str(self.suit)

