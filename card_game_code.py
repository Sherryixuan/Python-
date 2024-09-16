class Solitaire:
    def __init__(self, cards):
        self.piles = []
        self.num_cards = len(cards)
        self.num_piles = (self.num_cards // 8) + 3
        self.max_num_moves = self.num_cards * 2
        for i in range(self.num_piles):
            self.piles.append(CardPile())
        for i in range(self.num_cards):
            self.piles[0].add_bottom(cards[i])

    def get_pile(self, i):
        return self.piles[i]

    def display(self):
        for i in range(self.num_piles):
            if i == 0:
                lst = [str(self.get_pile(i).items[0]) if j == 0 else '*' for j in range(self.piles[i].size())]
                print(f"{i}: {' '.join(lst)}")
            else:
                pile = self.piles[i]
                print(f"{i}: ", end="")
                print(self.piles[i].print_all(i), end="")
                print()

    def move(self, p1, p2):
        if 0 <= p1 < len(self.piles) and 0 <= p2 < len(self.piles):
            pile1, pile2 = self.get_pile(p1), self.get_pile(p2)
            if p1 == 0 and p2 == 0:
                if pile1.size() != 0 and pile2.size() != 0:
                    top_card = pile1.remove_top()
                    pile1.add_bottom(top_card)
            elif p1 == 0 and p2 > 0:
                if pile1.size() != 0:
                    if pile2.size() == 0:
                        top_card = pile1.remove_top()
                        pile2.add_bottom(top_card)
                    else:
                        if pile1.peek_top() == pile2.peek_bottom() - 1:
                            top_card = pile1.remove_top()
                            pile2.add_bottom(top_card)
            elif p1 > 0 and p2 > 0:
                if pile1.size() != 0:
                    if pile2.size() != 0:
                        while pile1.size() != 0 and pile1.peek_top() == pile2.peek_bottom() - 1:
                            top_card = pile1.remove_top()
                            pile2.add_bottom(top_card)

                else:
                    if pile1.peek_top() == pile2.peek_bottom() - 1:
                        top_card = pile1.remove_top()
                        pile2.add_bottom(top_card)

    def is_complete(self):
        if self.get_pile(0).size() != 0:
            return False

        for i in range(1, self.num_piles):
            if self.get_pile(i).size() == self.num_cards:
                return True

        for i in range(1, self.num_piles):
            if not self.get_pile(i).items == sorted(self.get_pile(i).items, reverse=True):
                return False

        return False

    def play(self):
        print("********************** NEW GAME *****************************")
        move_number = 1
        while move_number <= self.max_num_moves and not self.is_complete():
            self.display()
            print("Round", move_number, "out of", self.max_num_moves, end=": ")
            row1 = int(input("Move from pile no.: "), 10)
            print("Round", move_number, "out of", self.max_num_moves, end=": ")
            row2 = int(input("Move to pile no.: "), 10)
            if row1 >= 0 and row2 >= 0 and row1 < self.num_piles and row2 < self.num_piles:
                self.move(row1, row2)
            move_number += 1

        if self.is_complete():
            print("You Win in", move_number - 1, "steps!\n")
            n = 0
            while n <= 5:
                
                try:
                    n = int(5)
                    print("*" + " " * (n - 2) + "*" * n)
                    for i in range(n - 2):
                        print("*" + " " * i + "*" + " " * (n - 3 - i) + "*" + (n - 3 - i) * " " + "*")
                    print("*" * (2 * n - 1))
                    for i in range(n - 2):
                        print(" " * (n - 2 - i) + "*" + " " * i + "*" + " " * i + "*" + (n - 3 - i) * " " + "*")
                    print(n * "*" + (n - 2) * ' ' + "*")
                    n+= 1
                except:
                    break
        else:
            print("You Lose!\n")
            n=0
            while n<=5:
                try:
                    n = int(5)
                    for i in range(1, n + 1):
                        print(" " * (n - i + 1) + "* " * i)
                    for i in range(n + 1, 0, -1):
                        print(" " * (n - i + 1) + "* " * i)
                    n += 5
                except:
                    break

class CardPile:
    def __init__(self):
        self.items = []

    def add_top(self, item):
        self.items.insert(0, item)

    def add_bottom(self, item):
        self.items.insert(self.size(), item)

    def remove_top(self):
        number = self.items.pop(0)
        return number

    def remove_bottom(self):
        number = self.items.pop(self.size() - 1)
        return number

    def size(self):
        return len(self.items)

    def peek_top(self):
        return self.items[0]

    def peek_bottom(self):
        return self.items[self.size() - 1]

    def print_all(self, index):
        if index == 0:
            string = ' *' * (self.size() - 1)
            return '{}{}'.format(self.peek_top(), string)
        elif index != 0:
            return ' '.join([str(i) for i in self.items])
import pygame
file="music.mp3"
pygame.mixer.init()
track=pygame.mixer.music.load(file)
pygame.mixer.music.play()



