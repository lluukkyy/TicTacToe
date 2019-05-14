import os
import pickle
import uuid

class classicGrid:
    def __init__(self, id = None, first = "o"):
        if id != None:
            idString = str(id)
            file = open("files/"+idString,"rb")
            self.grid = pickle.load(file)
            file.close()
            self.id = uuid.UUID(id)
        else:
            self.grid = [ [".",".","."],[".",".","."],[".",".","."] ]
            self.id = uuid.uuid4()
        self.winner = None
        self.next = "o"

    def put(self, row, col):
        if self.winner != None: return
        if self.grid[row][col] != ".": return
        self.grid[row][col] = self.next
        self.next = "x" if self.next == "o" else "o"
        self.check()

    def full(self):
        for i in self.grid:
            if "." in i: return False
        self.winner = "tie"
        return True

    def check3(self,x,y,z):
        if x != "." and x == y and y == z: 
            self.winner = x
            return True
        return False
    def check(self): 
        if self.full(): return
        for i in self.grid:
            if self.check3(i[0],i[1],i[2]): return
        for i in range(3):
            if self.check3(self.grid[0][i],self.grid[1][i],self.grid[2][i]): return
        if self.check3(self.grid[0][0],self.grid[1][1],self.grid[2][2]): return
        if self.check3(self.grid[0][2],self.grid[1][1],self.grid[2][0]): return

    def save(self):
        idString = str(self.id)
        file = open("files/"+idString,"wb")
        pickle.dump(self.grid,file)
        file.close()

    def __str__(self):
        return "\n----------\n".join([ " | ".join(i) for i in self.grid ])  
         
    