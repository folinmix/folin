class Square():
    sq_list=[]

    def __init__(self,sz):
        self.sz=sz
        self.sq_list.append(sz)

sq1=Square("sq1")
sq2=Square("sq2")

print(Square.sq_list)
