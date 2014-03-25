# http://www.codeskulptor.org/#user29_xOwzbCWVbZFWf1n.py
# template for "Stopwatch: The Game"
import simplegui

# define global variables
Time = 0
TenthOfSecond = 0
Seconds = 0
Minutes = 0
FormattedTime = ""
Attempts = 0
Success = 0
ScoreChangeAllowed = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global TenthOfSecond,Seconds,Minutes,FormattedTime,Success,Attempts
    TenthOfSecond = t % 10
    Seconds = t//10
    if Seconds >= 60 :
        Minutes = Seconds // 60
        Seconds = Seconds % 60
    FormattedTime = str(Minutes)+":"+str('%02d' % Seconds)+"."+str(TenthOfSecond)
    return FormattedTime

def score():
    global TenthOfSecond,Success,Attempts,ScoreChangeAllowed
    if ScoreChangeAllowed :
        if TenthOfSecond == 0 :
            Success = Success + 1
        Attempts = Attempts + 1
    ScoreChangeAllowed = False
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    global ScoreChangeAllowed
    ScoreChangeAllowed = True
    timer.start()
    

def stop_handler():
    timer.stop()
    score()
    
def reset_handler():
    timer.stop()
    global Time,Success,Attempts,ScoreChangeAllowed
    Time = 0
    Success = 0
    Attempts = 0
    ScoreChangeAllowed = False
    
# define event handler for timer with 0.1 sec interval
def tick():
    global Time
    Time = Time+1
    #print Time

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(str(format(Time)),[100,100],24,"White")
    canvas.draw_text(str(Success)+"/"+str(Attempts),[140,40],20,"White")
    
# create frame
frame = simplegui.create_frame("StopWatch",300,200)
timer = simplegui.create_timer(100,tick)
Start = frame.add_button("Start",start_handler,150)
Stop = frame.add_button("Stop",stop_handler,150)
Reset = frame.add_button("Reset",reset_handler,150)

# register event handlers
frame.set_draw_handler(draw_handler)

# start frame
frame.start()

# Please remember to review the grading rubric
