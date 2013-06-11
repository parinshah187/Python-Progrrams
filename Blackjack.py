# Blackjack URL :- http://www.codeskulptor.org/#user16_UgNvnfreSVkSo4q.py

import simplegui
import random

CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
class Hand:
    global VALUES,cards_string
    def __init__(self):
        # create Hand object
        self.card_list=[]
        self.value = 0
        self.cards_string = ""
        #print "Hand object created !"

    def __str__(self):
        i=0
        self.cards_string="Hand Contains : "
        # return a string representation of a hand
        while i<len(self.card_list) :
            self.cards_string+=self.card_list[i].suit+self.card_list[i].rank+" "
            #print i,"cards_string : ",self.cards_string
            i+=1
        cards_string = self.cards_string
        return self.cards_string
        
    def add_card(self, card):
        # add a card object to a hand
        self.card_list.append(card)
        #print "Card added to hand"
        

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        global cards_string
        i = 0
        acecount = 0
        self.value=0
        acecount = str(self).count("A")
        #print str(self)
        #print "acecount = ",acecount
        self.value += acecount*10
        #print "values : ",VALUES[str(self.card_list[i].rank)]
        while i<len(self.card_list):
            self.value+=int(VALUES[str(self.card_list[i].rank)])
            i+=1
        while self.value>21 and acecount>0:
            self.value-=10
            acecount-=1
        return self.value

    def draw(self, canvas, pos):
        i=0
        while i<len(self.card_list):
            self.card_list[i].draw(canvas,[pos[0]+(i*75),pos[1]])
            i+=1
       
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.deck = []
        count = 0
        for s in SUITS :
            for r in RANKS:
                self.deck.append(Card(s,r))
        print "Deck created"

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck)
        print "Deck shuffled"

    def deal_card(self):
        # deal a card object from the deck
        card = random.choice(self.deck)
        self.deck.remove(card)
        return card
    
    def __str__(self):
        # return a string representing the deck
        deck_string = "Deck contains : "
        for card in self.deck :
            deck_string+=card.suit+card.rank+" "
        return deck_string

# initialize some useful global variables
in_play = False
score = 0
player_hand = Hand()
dealer_hand = Hand()
deck = Deck()
pos = [150,420]
cards_string = ""
res = ""
player_points = 0
dealer_points = 0
    
#define event handlers for buttons
def deal():
    global in_play,player_hand,dealer_hand,deck,player_points,dealer_points,res
    res = ""
    player_points = 0
    dealer_points = 0
    player_hand = Hand()
    dealer_hand = Hand()
    #print "In deal(): res = ",res
     # your code goes here
    deck.shuffle()
    for i in range(2):
        player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())    
    in_play = True
    player_points = player_hand.get_value()
    dealer_points = dealer_hand.get_value()
    #print "Player's",player_hand,player_points
    #print "Dealer's",dealer_hand,dealer_points
    in_play = True

    
def hit():
    global deck,player_hand,res,player_points
    if in_play:
        c = deck.deal_card()
        player_hand.add_card(c)
        print c,player_hand.get_value()
        player_points = player_hand.get_value()
        if player_hand.get_value()>21:
            res+="Player is Busted ! Dealer Wins !"
        print "Player's",player_hand,player_hand.get_value()
        print "Dealer's",dealer_hand,dealer_hand.get_value()
        
       
def stand():
    global res,dealer_points,in_play
    if in_play:
        while dealer_hand.get_value()<17:
            c=deck.deal_card()
            dealer_hand.add_card(c)
        dealer_points = dealer_hand.get_value()        
        if dealer_hand.get_value()>21:
            res+="Dealer is Busted ! Player Wins !"
        else:
            if player_hand.get_value()>dealer_hand.get_value():
                res+="Player Wins !"
            else:
                res+="Dealer Wins !"
        in_play = False
        print "Player's",player_hand,player_hand.get_value()
        print "Dealer's",dealer_hand,dealer_hand.get_value()
        deal_available=True
    
    
# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text("Dealer",[270,40],30,"Black")
    canvas.draw_text("Points = "+str(dealer_points),[450,40],30,"Black")
    #canvas.draw_text("Result",[270,270],30,"Black")
    player_hand.draw(canvas,pos)
    dealer_hand.draw(canvas,[150,80])
    canvas.draw_text(res,[200,300],30,"Red")
    canvas.draw_text("Player",[250,570],30,"Black")
    canvas.draw_text("Points = "+str(player_points),[450,570],30,"Black")

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# Let's roll !
frame.start()
