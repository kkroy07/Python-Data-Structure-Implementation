class Human:
    def __init__(self,n,o):
        self.name = n
        self.occupation = o

    def do_work(self):
        if self.occupation=="tennis player":
            print(self.name," plays tennis")
        elif self.occupation=="actor":
            print(self.name," shoots a film")
    def speaks(self):
        print(self.name,"says how are you")

obj1=Human("Tom cruise","actor")
obj1.do_work()
obj1.speaks()
obj2=Human("Maria","tennis player")
obj2.do_work()
obj2.speaks()
