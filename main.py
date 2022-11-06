import time



class Game():
    def __init__(self):
        Game.print_mup(self)

    def create_map(self):
        map = []
        
        space = ''
        for i in range(50):
            space += '.'
        for x in range(25):
            map.append(space)

        self.map = map 

    def print_mup(self):
        Game.create_map(self)
        map = self.map

        print(len(map))
        for i in range(len(map)):
            print(map[i])
            time.sleep(0.02)

Game()
