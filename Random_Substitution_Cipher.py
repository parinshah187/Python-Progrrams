# URL -> http://www.codeskulptor.org/#user16_UjY3TZ9q0YH6c2e.py

import simplegui
import random

CIPHER = {}
LETTERS = "abcdefghijklmnopqrstuvwxyz"
msg = ""
emsg=""
en = True

def init():
    letter_list = list(LETTERS)
    random.shuffle(letter_list)
    for ch in LETTERS :
        CIPHER[ch] = letter_list.pop()
    print CIPHER        

def new_msg(m):
    global msg
    msg = m
    label.set_text(msg)
        
def encode():
    global msg,emsg,en
    emsg = ""
    for ch in msg :
        emsg += CIPHER[ch]
    msg = ""
    print msg,emsg
    en = True

def decode():
    global msg, emsg,en
    emsg = msg
    msg = ""
    for ch in emsg :
        for key in CIPHER :
            if CIPHER[key]==ch :
                msg+=key
    print emsg,"decoded as",msg
    en = False

def draw(canvas):
    if en :
        canvas.draw_text(emsg,[10,20],20,"White")
    else :
        canvas.draw_text(msg,[10,20],20,"White")
    
f = simplegui.create_frame("Cipher",200,200)
f.add_input("New Message : ",new_msg,200)
label = f.add_label("",200)
f.add_button("Encode",encode,100)
f.add_button("Decode",decode,100)
f.set_draw_handler(draw)
init()

f.start()
