class Player(object):
    def __init__(self, name, money, properties=None):
        self.name = name
        self.money = money
        if properties is None:
            self.properties = []
        else:
            self.properties = properties
