import sys
import time

map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 1,],
    [2, 0, 0, 0, 1, 1, 1, 1, 0, 1,],
    [1, 1, 0, 1, 1, 1, 1, 1, 0, 1,],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1,],
    [1, 0, 1, 0, 0, 1, 1, 0, 1, 1,],
    [1, 0, 0, 0, 0, 0, 0, 1, 1, 1,],
    [1, 1, 1, 1, 1, 0, 0, 1, 1, 1,],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1,]
]

def showMap ():
    print ()
    for  row in map:
        for item in row:
            if item == 1:
                print ("X", end="")
            elif str(item) == "$": print (" ", end="")
            elif (str(item) == "." or str(item) == "@"):
                print (item, end="")
            else:
                print (" ", end="")
        print ()
        
def action(x,y):
    if map[x][y] == 0:
        #map[x][y] = '@'
        #time.sleep(1)
        AI(x,y)
    if map[x][y] == 2:
        map[x][y] = '@'
        print ("FINISHED at line "+str(x)+" and column "+str(y))
        showMap()
        sys.exit()
        
def AI(x,y):
    map[x][y] = '.'
    action(x+1, y)
    action(x-1, y)
    action(x, y+1)
    action(x, y-1)
    map[x][y]='$'

AI(7, 6)
