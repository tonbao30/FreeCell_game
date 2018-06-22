from deck import*
from cards  import *

class Not_freecell:
    def __init__(self):
        self.game = deck_freecell()

    def __repr__(self):
        return 'Not_freecell()'

    #print out the string to guide the user input
    def __str__(self):
        move = "***pls input 'm <space> <main> <space> <target>' or 'move' the last card of a column within a cascade"
        free = "***pls input 'f <space> <target>' to move the last card in the target column to the freecells"
        foundations = "***pls input 's <space> <target>' to sort the last card in the target column to the foundation"
        unfree = "***pls input 'u <space> <freecell target> <space><cascade target>' to move the card from the freecells" \
                 "to the cascade or to the foundation"
        quiting = "***pls input QUIT in uppercase to quit the game"
        instruction = '\n'+'HOW TO PLAY:'+'\n' + move +'\n'+ free+ '\n' + foundations +'\n'+ unfree + '\n'\
                      + quiting +'\n'*2

        return instruction + str(self.game)

    #function to move the cards within the cascade
    def move(self, c1, c2):

        #find the card that users want to move in the cascade column
        for card_1 in self.game.cascade:
                for r1 in range(1,30):
                    if not self.game.is_empty(-r1,c1):
                        card_1 = self.game.cascade[-r1][c1]
                        break
                    elif self.game.is_empty(-r1,c1):
                        card_1 = self.game.is_empty(-r1,c1)
                        break

                #find the last card of the target column
                for r2 in range(1,30):
                    if not self.game.is_empty(-r2,c2):
                        card_2 = self.game.cascade[-r2][c2]
                        break
                    elif self.game.is_empty(-r2, c2):
                        card_2 = self.game.is_empty(-r2, c2)
                        break

        #check if it is a valid move based on the freecells rules
        try:
            if card_1.color == card_2.color:
                print("the cards must not be  in the same color")
            elif fullfaces.index(str(card_2.face)) - fullfaces.index(str(card_1.face)) != 1:
                print("the card's rank must lower than target")
            else:
                return self.game.add_card(self.game.get_card(c1), c2)


        #move the card in the empty target in the cascade
        except AttributeError:
            self.game.add_card(self.game.get_card(c1), c2)


    #function to move a card in cascade's columns  to a freecell
    def free(self, c):
        if self.game.freecells[0].count('--') == 0:
            print('the cells are full')
        else:
            for item_idx in range (0,4):
                if self.game.freecells[0][item_idx] == self.game.empty :
                    self.game.freecells[0][item_idx] = self.game.get_card(c)
                    break

            # Automatically sort card from free cells to the foundations
            for item_idx in range(0, 4):
                if self.game.freecells[0][item_idx] != self.game.empty :
                        for item_idx1 in range(0, 4):

                            # Automatically move Ace in free cells to foundations
                            if self.game.foundations[0][item_idx1] == self.game.empty:
                                if fullfaces.index(self.game.freecells[0][item_idx].face) == 1:
                                    self.game.foundations[0][item_idx1] = self.game.freecells[0][item_idx]
                                    self.game.freecells[0][item_idx] = self.game.empty
                                    break

                            # Automatically move next card in the sequence in free cells to foundations
                            elif self.game.foundations[0][item_idx1] != self.game.empty:
                                if fullfaces.index(self.game.foundations[0][item_idx1].face) \
                                        - fullfaces.index(self.game.freecells[0][item_idx].face) == - 1 :
                                    if self.game.foundations[0][item_idx1].suit == self.game.freecells[0][item_idx].suit:
                                        self.game.foundations[0][item_idx1] = self.game.freecells[0][item_idx]
                                        self.game.freecells[0][item_idx] = self.game.empty
                                    break

    #function to take the card from free cells and move to the cascade
    def unfree(self,i,c):

        #find the card in the free ceels
        for card_1 in self.game.freecells:
                if self.game.freecells[0][i] != self.game.empty:
                        card_1 = self.game.freecells[0][i]
                        for item_idx1 in range(0,4):

                            # unfree the card in the sequence in free cells to foundations
                            if self.game.foundations[0][item_idx1] != self.game.empty:
                                if fullfaces.index(self.game.foundations[0][item_idx1].face) \
                                        - fullfaces.index(card_1.face) == - 1:
                                    if self.game.foundations[0][item_idx1].suit == self.game.freecells[0][i].suit:
                                        self.game.foundations[0][item_idx1] = card_1
                                        self.game.freecells[0][i] = self.game.empty
                                    break
                else:
                    print('there is no card to move')
                    break

                # find the target in the cascade
                for card_2 in self.game.cascade:
                    for r2 in range(1, 30):
                        if not self.game.is_empty(-r2, c):
                            card_2 = self.game.cascade[-r2][c]
                        elif self.game.is_empty(-r2, c):
                            card_2 = self.game.is_empty(-r2, c)
                            break
                # check if it is a valid move based on the freecells rules
                try:
                    if card_1.color == card_2.color:
                        print("the card must not be in the same color")

                    elif fullfaces.index(str(card_2.face)) - fullfaces.index(str(card_1.face)) != 1:
                        print("the card must lower than target")
                    else:
                        self.game.add_card(self.game.freecells[0][i], c)
                        self.game.freecells[0][i] = self.game.empty

                # move the card if the target is an empty cascade
                except AttributeError:
                    self.game.add_card(self.game.freecells[0][i], c)
                    self.game.freecells[0][i] = self.game.empty

    #function sort the cards into foundations
    def sort(self,c):
        #find the card in the cascade
        for card in self.game.cascade:
            for r in range(1, 30):
                if not self.game.is_empty(-r, c):
                    card = self.game.cascade[-r][c]
                    break

        #check if the stack in the foundation is empty
        for item_idx in range(0, 4):
            if self.game.foundations[0][item_idx] == self.game.empty:
                if fullfaces.index(card.face) == 1:
                    self.game.foundations[0][item_idx] = self.game.get_card(c)
                    break
                else :
                    print('the first card must be ACE!!')
                    break

        #if the stack in the foundation have cards, check the last card of the stack to move the new card in based on
                    # freecell rules
            elif self.game.foundations[0][item_idx] != self.game.empty:
                if fullfaces.index(self.game.foundations[0][item_idx].face) - fullfaces.index(card.face) == -1:
                    if self.game.foundations[0][item_idx].suit == card.suit:
                        self.game.foundations[0][item_idx] = self.game.get_card(c)
                        break

    #function to check the player's commands
    def command(self, command):
        try:
            #move command, syntax: move or m <space><current column><space><target column>
            if command.startswith('m') or command.startswith('M'):
                words = command.split()
                c1 = int(words[1]) - 1
                c2 = int(words[2]) - 1
                self.move(c1,c2)

            #unfree command, syntax: unfree or u <space><current column><space><target column>
            elif command.startswith('u') or command.startswith('U'):
                words = command.split()
                i = int(words[1]) - 1
                c = int(words[2]) - 1
                self.unfree(i, c)

            #sort to foundation command, syntax: sort or s<space><target column>
            elif command.startswith('S') or command.startswith('s'):
                c = int(command.split()[1]) - 1
                self.sort(c)

            # free to freecells command, syntax: free or f<space><target column>

            elif command.startswith('F') or command.startswith('f'):
                words = command.split()
                c = int(words[1]) - 1
                self.free(c)

            #quit command
            elif command.startswith('Q') or command.startswith('q'):
                pass
            else:
                print('invalid input, pls read the instruction to play!!!')
        except ValueError:
            print('invalid input, pls read the instruction to play!!!')
        except IndexError:
            print('invalid input, pls read the instruction to play!!!')


    #function to loop the game until win or quit
    def play(self):
        # loop until game over/quit
        command = ''
        while not self.game_over() and 'QUIT' not in command:
            # show game and get command
            print(self)
            command = input("What's your play?  ")
            self.command(command)
        # check for game results
        else:
            print('game over.')

    #funtion to check if the game is over
    def game_over(self):
        for list in range(0):
            for item_idx,item in enumerate(list):
                if self.game.foundations[list][item_idx] != self.game.empty:
                    if all(fullfaces.index(self.game.foundations[list][item_idx].face) == 14
                           for self.game.foundations[list][item_idx] in self.game.foundations):
                        return True

def main():
    x = Not_freecell()
    x.play()
    x.game_over()
if __name__ == '__main__':
    main()









