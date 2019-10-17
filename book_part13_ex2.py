class Square():
    def __init__(self,s):
        self.size=s

    def ch_size(self,n):
        self.size+=n

sq1=Square(3)
sq1.ch_size(4)

print (sq1.size)

        
