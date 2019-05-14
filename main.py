import os
import sys
import random
from classicGrid import classicGrid

if __name__ == "__main__":
    count = 0
    while count <=1000:
        count+=1
        a = classicGrid()
        while a.winner == None:
            a.put(0,random.randint(0,8))  
        if a.winner != -1:
            print(count,":",a.winner,"wins!")
        else: 
            print(count,":","Game tied.")
        a.save2("save1")


    # a = classicGrid(id = "d3a8f31d-ae9e-471e-8b6a-fa5880333d3f")
    # print(a)