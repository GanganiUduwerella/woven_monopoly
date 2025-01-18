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

    @classmethod
    def fromJsonFile(cls, filename):
        
        with open(filename, 'r') as file:
            data = json.load(file)

        space_list = []

        for space_data in data:
            space_type = space_data.get("type")
            space_name = space_data.get("name")

            if space_type == "go":
                space = Go(spaceName=space_name, spaceType=space_type)
            elif space_type == "property":
                space_price = space_data.get("price", 0)
                space_colour = space_data.get("colour", "None")
                space = Property(spaceName=space_name, spaceType=space_type, spaceColour=space_colour, spacePrice=space_price)
            else:
                space = Space(spaceName=space_name, spaceType=space_type)

            
            space_list.append(space)

       
        return Board(spaceList=space_list)