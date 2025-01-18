class Player(object):
    def __init__(self, name, money, properties=None, currentPosition=0):
        self.name = name
        self.money = money
        if properties is None:
            self.properties = []
        else:
            self.properties = properties
        self.currentPosition = currentPosition
