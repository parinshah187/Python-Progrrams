# URL : - http://www.codeskulptor.org/#user16_tJ6bTfltxD8MBTT.py

import simplegui

# Map dimensions
MAP_HEIGHT = 1818
MAP_WIDTH = 1521

# Scaling factor
SCALE = 3

# Canvas dimensions
CAN_HEIGHT = MAP_HEIGHT // SCALE
CAN_WIDTH = MAP_WIDTH // SCALE

mag_pos=[CAN_WIDTH//2, CAN_HEIGHT//2]
MAG_SIZE = 120

# Define draw handler
def draw(canvas):
    global mag_pos,MAG_SIZE
    canvas.draw_image(im,
                      [MAP_WIDTH // 2, MAP_HEIGHT // 2],[MAP_WIDTH,MAP_HEIGHT],
                      [CAN_WIDTH // 2, CAN_HEIGHT // 2],[CAN_WIDTH,CAN_HEIGHT])
    # Draw Magnifier
    map_center = [SCALE * mag_pos[0] , SCALE * mag_pos[1]]
    mag_center = mag_pos
    mag_rect = [MAG_SIZE,MAG_SIZE]
    canvas.draw_image(im,map_center,mag_rect,mag_center,mag_rect)
    # Above line states to draw mag_rect portion of original map at mag_center

# Define Mouse-click handlers
def click(pos) :
    global mag_pos
    mag_pos = list(pos)
    
# Create frame,set event handlers and load image
f = simplegui.create_frame("Map Magnifier",CAN_WIDTH,CAN_HEIGHT)
im = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/gutenberg.jpg")
f.set_mouseclick_handler(click)
f.set_draw_handler(draw)

# Start the frame
f.start()
