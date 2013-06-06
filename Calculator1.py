# URL : http://www.codeskulptor.org/#user11_2qBOs6XxHM_1.py

import simplegui
store = 0
operand = 0

def enter(inp):
    global store,operand
    operand = float(inp)
    output()
    
def output() :
    print "Store : ",store
    print "Operand : ",operand
    print "\n"

def swap():
    global store,operand
    store,operand = operand,store
    output()

def add():
    global store,operand
    store = store + operand
    output()

def sub():
    global store,operand
    store = store - operand
    output()

def mul():
    global store,operand
    store = store * operand
    output()
    
def div():
    global store,operand
    store = store / operand
    output()
    
f = simplegui.create_frame("Calculator",200,300)
f.add_button("Print",output,100)
f.add_button("Swap",swap,100)
f.add_button("Add",add,100)
f.add_button("Subtract",sub,100)
f.add_button("Multiply",mul,100)
f.add_button("Divide",div,100)
f.add_input("Enter a number ",enter,100)
