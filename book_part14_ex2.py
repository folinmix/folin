class Square():
    def __init__(self,sz):
        self.sz=str(sz)

    def __repr__(self):
        return self.sz+' �� '+self.sz+' �� '+self.sz+' �� '+self.sz

sq1=Square(29)

print(sq1)
