import pyautogui
import random
import sys

if len(sys.argv)==1:
    MOVES=6
else:
    MOVES = int(sys.argv[-1])

print('MOVES',MOVES)
GAP=100
choices= [1,2,3,4]
removes={1:[1,4],2:[2,3],3:[3,2],4:[1,4]}
sizes = pyautogui.size()
halfx,halfy = sizes[0]//2,sizes[1]//2

points={}
points[1]=(GAP,GAP)
points[2]=(sizes[0]-GAP,GAP)
points[3]=(GAP,sizes[1]-GAP)
points[4]=(sizes[0]-GAP,sizes[1]-GAP)

places=[1]
pyautogui.moveTo(points[1][0],points[1][1])
for _ in range(MOVES):
    if places[-1] in [1,4]:
        temp=[2,3]
    else:
        temp=[1,4]
    c = random.choice(temp)
    places.append(c)

for i in places:
    pyautogui.moveTo(points[i][0],points[i][1],1)

pyautogui.alert('Movement Done! Ready to follow?')

pyautogui.moveTo(points[1][0],points[1][1])

gameOn=True

gameplace = 0
while gameOn:
    if gameplace==MOVES+1:
        break
    cX, cY = pyautogui.position()
    if cX > halfx and cY> halfy:
        curpos=4
    elif cX>halfx and cY<halfy:
        curpos=2
    elif cX<halfx and cY> halfy:
        curpos=3
    elif cX<halfx and cY< halfy:
        curpos=1
    if gameplace==0 and curpos!=1:
        if places[gameplace]==curpos:
            gameplace+=1
            continue
        else:
            gameOn = False
            break
    if curpos!=places[gameplace]:
        if curpos == places[gameplace-1]:
            continue
        else:
            gameOn = False
            break
    else:
        gameplace+=1
        continue

if gameplace<MOVES+1:
    pyautogui.alert('You Have Lost')
else:
    pyautogui.alert('You Won!! Nice one.')
print("Game Ended")

    