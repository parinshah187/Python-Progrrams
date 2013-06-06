# http://www.codeskulptor.org/#user12_XKmr3YL1ip_2.py

import simplegui

val = 3.12

def draw_handler(canvas):
    canvas.draw_text(str(val),[100,100],24,"White")
    
def convert(a):
    dol = round(a)
    cents = round((a - dol) * 100)
    global val
    val = str(dol)+ " dollars and "+str(cents)+" cents"
    
    
def input_handler(inp):
    global val
    convert(float(inp))
    

frame = simplegui.create_frame("Test",400,400)

frame.set_draw_handler(draw_handler)
inp = frame.add_input("Enter value :",input_handler,50)

frame.start()
