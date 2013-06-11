# URL :- http://www.codeskulptor.org/#user16_friQqCv7PuFWAOc.py
import simplegui
import random

cards = []
deck = []
exposed = []
state = 0
clicked_cards=[0,0]
first_card=True
move = 0
# helper function to initialize globals
def init():
    global cards,deck,exposed,first_card,clicked_cards,move
    cards = [0,1,2,3,4,5,6,7]
    deck = list(cards)
    random.shuffle(deck)
    deck2 = list(deck)
    random.shuffle(deck2)
    deck.extend(deck2)
    random.shuffle(deck)
    exposed = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    first_card=True
    clicked_cards=[0,0]
    move = 0
     
# define event handlers

# initialize global variables
init()
    
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global deck,exposed,move
    canvas.draw_polygon([[0,0],[0,100],[50,100],[50,0]],2,"Red","Green")
    label.set_text("moves = "+str(move))
    for c in range(16):
        if exposed[c]:
            canvas.draw_polygon([[(c*50)+0,0],[(c*50)+0,100],[(c+1)*50,100],[(c+1)*50,0]],2,"Red","Black")
            canvas.draw_text(str(deck[c]),[2+(50*c),80],80,"White")
        else:
            canvas.draw_polygon([[(c*50)+0,0],[(c*50)+0,100],[(c+1)*50,100],[(c+1)*50,0]],2,"Red","Green")

def click(pos):
    global deck,exposed,state,clicked_cards,first_card,move
    if state==0:
        state=1
    elif state==1:
        state=2
    else :
        state=1
        if deck[clicked_cards[0]]!=deck[clicked_cards[1]]:
            exposed[clicked_cards[0]]=False
            exposed[clicked_cards[1]]=False
    if first_card:
        clicked_cards[0]=(pos[0]//50)
        first_card=False
        exposed[clicked_cards[0]]=True
    else:
        clicked_cards[1]=(pos[0]//50)
        first_card=True
        exposed[clicked_cards[1]]=True
        move+=1

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", init)
label = frame.add_label("Moves = 0")

# register event handlers
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)

# get things rolling
frame.start()
