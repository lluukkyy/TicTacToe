import os
import sys
from classicGrid import classicGrid

if __name__ == "__main__":
    a = classicGrid()
    while not a.winner:
        print(a)
        cmd = input("Put \""+a.next+"\" at: ")
        cmd = [int (i)  for i in cmd.strip().split()]
        if len(cmd) != 2: continue
        a.put(cmd[0],cmd[1])  
    if a.winner != "tie":
        print(a.winner,"wins! Saving as", a.id)
    else: 
        print("Game tied.")
    a.save()


    # a = classicGrid(id = "d3a8f31d-ae9e-471e-8b6a-fa5880333d3f")
    # print(a)