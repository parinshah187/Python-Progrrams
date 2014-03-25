URL : http://www.codeskulptor.org/#user29_dDUyFdHjHL3Q8dd.py

# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random

# initialize global variables used in your code
var2 = 0
attempts_left = 0
game_status = "Press Range buttons"
attempts=0
msg = ""

# define event handlers for control panel
def init():
    range100()

# draw handler
def draw(canvas):
    global game_status,attempts,msg
    canvas.draw_text(game_status,[100,280],20,"Red")
    canvas.draw_text("Attempts remaining : "+str(attempts),[100,20],20,"Red")
    canvas.draw_text(msg,[100,150],20, "Red")
    
def range100():
    # button that changes range to range [0,100) and restarts
    global attempts_left, var2, game_status,attempts
    attempts_left = 7
    var2 = random.randrange(0,100)
    game_status="New Game. Range is 0 to 100"
    attempts=7;
    print "New Game. Range is 0 to 100 "
    print "Number of attempts remaining : ",attempts_left
    
def range1000():
    # button that changes range to range [0,1000) and restarts
    global attempts_left, var2, game_status, attempts
    attempts_left = 10
    var2 = random.randrange(0,1000)
    game_status="New Game. Range is 0 to 1000"
    attempts=10;
    print "New Game. Range is 0 to 1000"
    print "Number of attempts remaining : ",attempts_left

def get_input(guess):
    # main game logic goes here	
    global attempts_left, var2, game_status, attempts, msg
    attempts_left = attempts_left - 1
    attempts = attempts-1
    guess = int(guess)
    if attempts_left==0 :
        if guess!=var2 :
            print "Sorry, your guess was incorrect ! Correct answer is ",var2,".! Game over !"
            msg = "Sorry, your guess was incorrect ! Correct answer is "+str(var2)+".! Game over !"
            init()
        elif guess==var2 :
            print "Bingo ! Correct answer is :",var2," !\n"
            msg = "Bingo ! Correct answer is :"+str(var2)+" !\n"
            init()
    
    elif attempts_left==0 & guess==var2:
        print "Bingo ! Correct answer is :",var2," !\n"
        msg = "Bingo ! Correct answer is :"+str(var2)+" !\n"
        init()
        
    else :
        guess = int(guess)
        if var2<guess :
            print "Guess LOWER number"
            msg = "Guess LOWER number"
        elif var2>guess :
            print "Guess HIGHER number"
            msg = "Guess HIGHER number"
        else :
            print "Bingo ! Press button of your selected range to restart game"
            msg = "Bingo ! Press button of your selected range to restart game"
            init()
        print attempts_left," attempts remaining"


frame=simplegui.create_frame("Guess the number", 600,300)
frame.set_canvas_background("White")


# register event handlers for control elements
frame.add_button("Range is [0,100)",range100,200)
frame.add_button("Range is [0,1000)",range1000,200)
frame.add_input("Enter a guess ",get_input,200)
frame.set_draw_handler(draw)

frame.start()
