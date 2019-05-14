import os


class classicGrid:
    def __init__(self, first = 0):
        self.grid = [-1] * 9
        self.winner = None
        self.next = 0

    def put(self, row, col):
        if self.winner != None: return
        index = row * 3 + col
        if self.grid[index] != -1: return
        self.grid[index] = self.next
        self.next = 1 if self.next == 0 else 0
        self.check()

    def full(self):
        if -1 in self.grid: return False
        self.winner = -1
        return True

    def check3(self,x,y,z):
        if x != -1 and x == y and y == z: 
            self.winner = x
            return True
        return False
    def check(self): 
        for i in range(3):
            if self.check3(self.grid[i * 3],self.grid[i * 3 + 1],self.grid[i * 3 + 2]): return
            if self.check3(self.grid[i],self.grid[3+i], self.grid[6+i]): return
        if self.check3(self.grid[0], self.grid[4], self.grid[8]): return
        if self.check3(self.grid[2],self.grid[4],self.grid[6]): return
        if self.full(): return

    def save2(self, filename):
        file = open("files/"+filename+".txt","a+")
        file.write("{} {}\n".format(" ".join(map(str,self.grid)),str( self.winner)))
        file.close()

    def __str__(self):
        return "\n----------\n".join([ " | ".join( map(str,self.grid[i*3: i*3+3])) for i in range(3) ])  
         
    