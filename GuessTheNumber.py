# http://www.codeskulptor.org/#user11_LYdu5dnfvDYYarn.py
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random

# initialize global variables used in your code
var2 = 0
attempts_left = 0

# define event handlers for control panel

def init():
    range100()
    

def range100():
    # button that changes range to range [0,100) and restarts
    global attempts_left, var2
    attempts_left = 7
    var2 = random.randrange(0,100)
    print "New Game. Range is 0 to 100 "
    print "Number of attempts remaining : ",attempts_left

def range1000():
    # button that changes range to range [0,1000) and restarts
    global attempts_left, var2
    attempts_left = 10
    var2 = random.randrange(0,1000)
    print "New Game. Range is 0 to 1000"
    print "Number of attempts remaining : ",attempts_left

def get_input(guess):
    # main game logic goes here	
    global attempts_left, var2
    attempts_left = attempts_left - 1
    guess = int(guess)
    if attempts_left==0 :
        if guess!=var2 :
            print "Sorry, your guess was incorrect ! Correct answer is ",var2,".! Game over !\n"
            init()
        elif guess==var2 :
            print "Bingo ! Correct answer is :",var2," !\n"
            init()
    
    elif attempts_left==0 & guess==var2:
        print "Bingo ! Correct answer is :",var2," !\n"
        init()
        
    else :
        guess = int(guess)
        if var2<guess :
            print "Guess LOWER number"
        elif var2>guess :
            print "Guess HIGHER number"
        else :
            print "Bingo ! Press button of your selected range to restart game"
            init()
        print attempts_left," attempts remaining"
    
# create frame
f = simplegui.create_frame("Guess the number",200,300)

# register event handlers for control elements
f.add_button("Range is [0,100)",range100,200)
f.add_button("Range is [0,1000)",range1000,200)
f.add_input("Enter a guess ",get_input,200)

# start frame
f.start
init()

# always remember to check your completed program against the grading rubric
