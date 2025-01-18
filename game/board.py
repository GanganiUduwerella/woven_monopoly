import json


class Space(object):
    def __init__(self, spaceName, spaceType):
        self.spaceName = spaceName
        self.spaceType = spaceType
        self.occupants = []
    

class Go(Space):
    def __init__(self, spaceName, spaceType):
        super().__init__(spaceName, spaceType)


class Property(Space):
    def __init__(self, spaceName, spaceType, spaceColour, spacePrice):
        super().__init__(spaceName, spaceType)
        self.spaceColour = spaceColour
        self.spacePrice = spacePrice
        self.owner = None


class Board(object):
    def __init__(self, spaceList=None):
        if spaceList is None:
            self.spaceList = []
        else:
            self.spaceList = spaceList
    
    def ownerSameForColorOf(self, propertySpace):
        propertyList = [space for space in self.spaceList if isinstance(space, Property)]
        sameColorProperies = [p for p in propertyList if p.spaceColour == propertySpace.spaceColour]
        ownerSameForColor = [p.owner == propertySpace.owner for p in sameColorProperies]
        return all(ownerSameForColor)

    @classmethod
    def fromJsonFile(cls, filename):
        
        with open(filename, 'r') as file:
            data = json.load(file)

        spaceList = []

        for spaceData in data:
            spaceType = spaceData.get("type")
            spaceName = spaceData.get("name")

            if spaceType == "go":
                space = Go(spaceName=spaceName, spaceType=spaceType)
            elif spaceType == "property":
                space_price = spaceData.get("price", 0)
                space_colour = spaceData.get("colour", "None")
                space = Property(spaceName=spaceName, spaceType=spaceType, spaceColour=space_colour, spacePrice=space_price)
            else:
                space = Space(spaceName=spaceName, spaceType=spaceType)

            
            spaceList.append(space)

       
        return Board(spaceList=spaceList)
    