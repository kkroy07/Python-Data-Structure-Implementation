class Father():
    def __init__(self):
        print("I am father")
    def coding(self):
        print("I love coding")

class Mother():
    def __init__(self):
        print("I am mother")
    def cooking(self):
        print("I love cooking")

class child(Father,Mother):
    def __init__(self):
        f=Father()
        m=Mother()
        print("I am child")
    def playing(self):
        print("I love playing football")

c=child()
c.coding()
c.cooking()
c.playing()
