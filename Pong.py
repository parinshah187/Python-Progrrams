# URL :- http://www.codeskulptor.org/#user15_rnh6Gl1bRkJ9G8b.py

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
ball_pos = [WIDTH/2,HEIGHT/2]
paddle1_pos = [[0,(HEIGHT/2)-(PAD_HEIGHT/2)],[PAD_WIDTH,(HEIGHT/2)-(PAD_HEIGHT/2)],[PAD_WIDTH,(HEIGHT/2)+(PAD_HEIGHT/2)],[0,(HEIGHT/2)+(PAD_HEIGHT/2)]]
paddle2_pos = [[WIDTH-PAD_WIDTH-1,(HEIGHT/2)-(PAD_HEIGHT/2)],[WIDTH-1,(HEIGHT/2)-(PAD_HEIGHT/2)],[WIDTH-1,(HEIGHT/2)+(PAD_HEIGHT/2)],[WIDTH-PAD_WIDTH-1,(HEIGHT/2)+(PAD_HEIGHT/2)]]
paddle1_vel = 0
paddle2_vel = 0
score1_pos = [(WIDTH/2)-150,100]
score2_pos = [(WIDTH/2)+150,100]
score1 = 0
score2 = 0
right = False

# helper function that spawns a ball by updating the 
# ball's position vector and velocity vector
# if right is True, the ball's velocity is upper right, else upper left
def ball_init(right):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2,HEIGHT/2]
    if right :
        ball_vel = [int(-random.randrange(120, 240)) /60,int(-random.randrange(60, 180))/60]
        #ball_vel = [random.randrange(12,24),-random.randrange(6, 18)]
    else:
        ball_vel = [int(random.randrange(120, 240)) /60,int(-random.randrange(60, 180))/60]
    


# define event handlers

def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
    global score1, score2  # these are ints
    score1=0
    score2 =0
    ball_init(False)

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel,right
    
 #ball reflects from left paddle
    if ball_pos[0] <=(BALL_RADIUS + PAD_WIDTH)and ball_pos[1]>=paddle1_pos[1][1] and ball_pos[1]<=paddle1_pos[2][1]:
        ball_vel[0] = -ball_vel[0]
        ball_pos[0] += ball_vel[0]
        ball_pos[1] += ball_vel[1]
        ball_vel[0]+=0.5
        ball_vel[1]+=0.5
        
 #ball reflects from right paddle       
    if ball_pos[0] >=((WIDTH-1)-BALL_RADIUS - PAD_WIDTH)and ball_pos[1]>=paddle2_pos[0][1] and ball_pos[1]<=paddle2_pos[3][1]:
        ball_vel[0] = -ball_vel[0]
        ball_pos[0] += ball_vel[0]
        ball_pos[1] += ball_vel[1]
        ball_vel[0]-=0.5
        ball_vel[1]+=0.5
        
 # ball hits left gutter
    if ball_pos[0] <=(BALL_RADIUS + PAD_WIDTH)and (ball_pos[1]>=paddle1_pos[2][1] or ball_pos[1]<=paddle1_pos[1][1]):
        print "left gutter"
        score2+=1
        if right==True:
            right=False
        ball_init(right)
        
 # ball hits right gutter
    if ball_pos[0] >=((WIDTH-1)-BALL_RADIUS - PAD_WIDTH)and (ball_pos[1]>=paddle2_pos[0][1] or ball_pos[1]<=paddle2_pos[3][1]):
            print "right gutter"
            score1+=1
            if right==False:
                right=True
            ball_init(right)     
        
    # update paddle's vertical position, keep paddle on the screen
    if (paddle1_pos[0][1]+paddle1_vel)<= 0 :
            paddle1_vel=0
    if (paddle1_pos[2][1]+paddle1_vel)>= HEIGHT :
            paddle1_vel=0

            
    paddle1_pos[0][1]+=paddle1_vel
    paddle1_pos[1][1]+=paddle1_vel
    paddle1_pos[2][1]+=paddle1_vel
    paddle1_pos[3][1]+=paddle1_vel
    
    if (paddle2_pos[0][1]+paddle2_vel)<= 0 :
            paddle2_vel=0
    if (paddle2_pos[2][1]+paddle2_vel)>= HEIGHT :
            paddle2_vel=0
    
    paddle2_pos[0][1]+=paddle2_vel
    paddle2_pos[1][1]+=paddle2_vel
    paddle2_pos[2][1]+=paddle2_vel
    paddle2_pos[3][1]+=paddle2_vel
        
    
    
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # draw paddles
    c.draw_polygon(paddle1_pos,1, "Black","Yellow")
    c.draw_polygon(paddle2_pos,1, "Black","Yellow")
    
    # update ball
 
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    if  ball_pos[1] >=HEIGHT-BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    ball_pos[0]+=ball_vel[0]
    ball_pos[1]+=ball_vel[1]
    
    # draw ball and scores
    c.draw_circle(ball_pos,BALL_RADIUS,1,"Red","White")
    c.draw_text(str(score1), score1_pos, 48,"red")
    c.draw_text(str(score2), score2_pos,48,"red")
    
def keydown(key):
    global paddle1_vel,paddle1_pos, paddle2_pos, paddle2_vel,flag_left1, flag_left2, flag_right1, flag_right2
    print paddle1_vel
    if paddle1_pos[0][1]>0 and chr(key)=='W' :
        paddle1_vel -= 3
    if chr(key)=='S' :
        paddle1_vel += 3
        
    if key==simplegui.KEY_MAP["up"] :
        paddle2_vel -= 3
    if key==simplegui.KEY_MAP["down"] :
        paddle2_vel += 3
    
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    
    if chr(key)=='W':
        paddle1_vel=0

    elif chr(key)=='S':
        paddle1_vel=0

    if key==simplegui.KEY_MAP["up"]:
        paddle2_vel=0

    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel=0
    
def restart():
    new_game()
    
    
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart",restart)
new_game()

# start frame
frame.start()
