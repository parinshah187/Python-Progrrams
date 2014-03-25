# http://www.codeskulptor.org/#user29_xqQz0cHfPRqbeUR.py
# Rock-paper-scissors-lizard-Spock


# Equating the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# functions
import random 
def number_to_name(number):
    # converts number to a name
    if number==0:
        name = "rock"
    elif number==1:
        name="Spock"
    elif number==2:
        name="paper"
    elif number==3:
        name="lizard"
    elif number==4:
        name="scissors"
    else:
        print number
        name="Invalid number"
    return name

    
def name_to_number(name):
    # converts name to number
    if name=="rock":
        number=0
    elif name=="Spock":
        number=1
    elif name=="paper":
        number=2
    elif name=="lizard":
        number=3
    elif name=="scissors":
        number=4
    else :
        print name
        number=-1
    return number


def rpsls(name): 
      
    # converts name to player_number using name_to_number
    player_number = name_to_number(name)
    # computes random guess for comp_number using random.randrange()
    comp_number=random.randrange(0,5,1)
    # computes difference of player_number and comp_number modulo five
    diff = (comp_number-player_number)%5
    # determines winner
    if diff==0:
        flag=0
    elif diff<=2:
        flag=1
    else:
        flag=2
    
    # converts comp_number to name using number_to_name
    print "Player chooses", number_to_name(player_number)
    print "Computer chooses", number_to_name(comp_number)
    # print results
    if flag==0:
        print "Computer and Player tie","\n"
    elif flag==1:
        print "Computer wins !","\n"
    elif flag==2:
        print "Player wins !","\n"
    
# test cases
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")


