import time


class TrafficLigth:
    color = ['red', 'yellow', 'green']

    def running(self):
        while True:
            print(TrafficLigth.color[0])
            time.sleep(7)
            print(TrafficLigth.color[1])
            time.sleep(2)
            print(TrafficLigth.color[2])
            time.sleep(4)


tl = TrafficLigth()
tl.running()