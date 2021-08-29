from random import shuffle

def createDeck():
    Deck = []
    cardSuits = [u'\u2660', u'\u2665', u'\u2666', u'\u2663']
    faceValues = ['A', 'J', 'Q', 'K']

    #generate 4 sets of cards
    for i in cardSuits:
        for card in range (2, 11):
            Deck.append('{}{}'.format(card, i))

        for card in faceValues:
            Deck.append('{}{}'.format(card, i))
    shuffle(Deck)

    return Deck

class Player:
    def __init__(self, hand = [], money = 100):
        self.hand = hand
        self.score = self.setScore()
        self.money = money
        self.bet = 0

    def __str__(self):
        currentHand = ''
        for card in self.hand:
            currentHand += card + ' '
        finalStatus = currentHand + '\nscore: {}'.format(self.score)
        return finalStatus
    
    def setScore(self):
        self.score = 0
        faceCardsDict = {'2{}'.format(u'\u2660'): 2, '3{}'.format(u'\u2660'): 3,
        '4{}'.format(u'\u2660'): 4, '5{}'.format(u'\u2660'): 5, '6{}'.format(u'\u2660'): 6,
        '7{}'.format(u'\u2660'): 7, '8{}'.format(u'\u2660'): 8, '9{}'.format(u'\u2660'): 9,
        '10{}'.format(u'\u2660'): 10, 'J{}'.format(u'\u2660'): 10, 'Q{}'.format(u'\u2660'): 10,
        'K{}'.format(u'\u2660'): 10, 'A{}'.format(u'\u2660'): 11, '2{}'.format(u'\u2665'): 2,
        '3{}'.format(u'\u2665'): 3, '4{}'.format(u'\u2665'): 4, '5{}'.format(u'\u2665'): 5,
        '6{}'.format(u'\u2665'): 6, '7{}'.format(u'\u2665'): 7, '8{}'.format(u'\u2665'): 8,
        '9{}'.format(u'\u2665'): 9, '10{}'.format(u'\u2665'): 10, 'J{}'.format(u'\u2665'): 10,
        'Q{}'.format(u'\u2665'): 10, 'K{}'.format(u'\u2665'): 10, 'A{}'.format(u'\u2665'): 11,
        '2{}'.format(u'\u2666'): 2, '3{}'.format(u'\u2666'): 3, '4{}'.format(u'\u2666'): 4,
        '5{}'.format(u'\u2666'): 5, '6{}'.format(u'\u2666'): 6, '7{}'.format(u'\u2666'): 7,
        '8{}'.format(u'\u2666'): 8, '9{}'.format(u'\u2666'): 9, '10{}'.format(u'\u2666'): 10,
        'J{}'.format(u'\u2666'): 10, 'Q{}'.format(u'\u2666'): 10, 'K{}'.format(u'\u2666'): 10,
        'A{}'.format(u'\u2666'): 11, '2{}'.format(u'\u2663'): 2, '3{}'.format(u'\u2663'): 3,
        '4{}'.format(u'\u2663'): 4, '5{}'.format(u'\u2663'): 5, '6{}'.format(u'\u2663'): 6,
        '7{}'.format(u'\u2663'): 7, '8{}'.format(u'\u2663'): 8, '9{}'.format(u'\u2663'): 9,
        '10{}'.format(u'\u2663'): 10, 'J{}'.format(u'\u2663'): 10, 'Q{}'.format(u'\u2663'): 10,
        'K{}'.format(u'\u2663'): 10, 'A{}'.format(u'\u2663'): 11}
        aceCounter = 0
        for card in self.hand:
            self.score += faceCardsDict[card]
            if card == 'A':
                aceCounter += 1
            if self.score > 21 and aceCounter != 0:
                self.score -= 10
                aceCounter -= 1
        return self.score
    
    def hit(self, card):
        self.hand.append(card)
        self.score = self.setScore()

    def play(self, newHand):
        self.hand = newHand
        self.score = self.setScore()

    def betMoney(self, amount):
        self.money -= amount
        self.bet += amount
    
    def win(self, result):
        if result == True:
            if self.score == 21 and len(self.hand) == 2:
                self.money += 2.5*self.bet
            else:
                self.money += 2*self.bet
            self.bet = 0
        else:
            self.bet = 0

    def hasBlackjack(self):
        if self.score == 21 and len(self.hand) == 2:
           return True
        else:
            return False
    
    def draw(self):
        self.money += self.bet
        self.bet = 0

def printHouse(house):
    for card in range(len(house.hand)):
        if card == 0:
            print('X', end = ' ')
        elif card == len(house.hand) - 1:
            print(house.hand[card])
        else:
            print(house.hand[card], end = ' ')

cardDeck = createDeck()
# print(cardDeck)

firstHand = [cardDeck.pop(), cardDeck.pop()]
secondHand = [cardDeck.pop(), cardDeck.pop()]

player1 = Player(firstHand)
house = Player(secondHand)

cardDeck = createDeck()
while(True):
    if len(cardDeck) < 20:
        cardDeck = createDeck()
    firstHand = [cardDeck.pop(), cardDeck.pop()]
    secondHand = [cardDeck.pop(), cardDeck.pop()]

    player1.play(firstHand)
    house.play(secondHand)
    
    playerBet = int(input('Please enter the bet: '))
    player1.betMoney(playerBet)

    print('Player:\n', player1, '\n')
    print('House:')
    printHouse(house)

    if player1.hasBlackjack():
        if house.hasBlackjack():
            player1.draw()
        else:
            player1.win(True)
    # elif house.hasBlackjack():
    #     house.win(True)
    else:
        while(player1.score < 21):
            action = input('\nDo you want another card? [Y/N]: ')
            if action == 'Y' or action =='y':
                player1.hit(cardDeck.pop())
                print(player1)
                printHouse(house)
            else:
                break

        while(house.score < 16):
            house.hit(cardDeck.pop())
        
        if player1.score > 21:
            if house.score > 21:
                player1.draw()
            else:
                player1.win(True)
        elif player1.score > house.score:
            player1.win(True)
        elif player1.score == house.score:
            player1.draw()
        else:
            if house.score > 21:
                player1.win(True)
            else:
                player1.win(False)

    print(player1.money, '\n')
    print(house)                                