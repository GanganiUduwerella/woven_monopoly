class Space(object):
    def __init__(self, spaceName, spaceType):
        self.spaceName = spaceName
        self.spaceType = spaceType


class Go(Space):
    def __init__(self, spaceName, spaceType):
        super().__init__(spaceName, spaceType)


class Property(Space):
    def __init__(self, spaceName, spaceType, spaceColour, spacePrice):
        super().__init__(spaceName, spaceType)
        self.spaceColour = spaceColour
        self.spacePrice = spacePrice


class Board(object):
    def __init__(self, spaceList=None):
        if spaceList is None:
            self.spaceList = []
        else:
            self.spaceList = spaceList
