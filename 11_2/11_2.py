class Road:

    def __init__(self):
        self.length = None
        self.width = None

    def result(self):
        print(round(self.length*self.width*25*0.005))


r = Road()
r.length = 5000
r.width = 20
r.result()
