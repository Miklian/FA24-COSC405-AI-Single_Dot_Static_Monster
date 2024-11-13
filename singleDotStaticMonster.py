from SingleDotProblemStaticMonster import Agent, State, Problem
from problemGraphics import pacmanGraphic
import random

p = Problem('singleDotSmall.txt')
#p = Problem('singleDotMedium.txt')

def prt(V):
    for k in V:
        print(k.agentPos, V[k])

# Complete your code here for
# value iteration and extract policy



# ------ END of your code ----------------

pac = pacmanGraphic(1300, 700)
pac.setup(p)


for k in policy:
    s = None
    if policy[k] == 'L': s = '\u2190'   # Prints left arrow
    if policy[k] == 'R': s = '\u2192'   # Prints right arrow
    if policy[k] == 'U': s = '\u2191'   # Prints up arrow
    if policy[k] == 'D': s = '\u2193'   # Prints down arrow
    
    if s: pac.addText(k.agentClass.pos[0]+0.5, k.agentClass.pos[1]+0.5, s, fontSize=20)

print('Apply policy')
currentState = p.getStartState()
count = 0
while currentState:
    a = policy[currentState]
    if a == None: break
    count+=1
    dx, dy = p.potential_moves[a]
    agentPos = (currentState.agentClass.pos[0] + dx, currentState.agentClass.pos[1] + dy)
    if agentPos in p.dots:
        index = p.dots.index(agentPos)
        pac.remove_dot(index)
    currentState = State(agentPos)
    pac.move_pacman(dx, dy)
    

print('plan length=', count)

