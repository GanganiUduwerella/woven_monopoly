import json


class Space(object):
    """
    Represents a generic space on the board, which can be extended into
    specific types: 'Go' or 'Property'.
    """

    def __init__(self, spaceName, spaceType):
        """
        Initializes a Space instance.

        Args:
            spaceName (str): The name of the space.
            spaceType (str): The type of the space.
        """
        self.spaceName = spaceName
        self.spaceType = spaceType
        self.occupants = []


class Go(Space):
    """
    Represents the 'Go' space on the board where players collect money when they pass it.
    """

    def __init__(self, spaceName, spaceType):
        """
        Initializes a Go space.

        Args:
            spaceName (str): The name of the Go space.
            spaceType (str): The type of the space ('go').
        """
        super().__init__(spaceName, spaceType)


class Property(Space):
    """
    Represents a property space that can be bought, sold, or rented by players.
    """

    def __init__(self, spaceName, spaceType, spaceColour, spacePrice):
        """
        Initializes a Property space.

        Args:
            spaceName (str): The name of the property.
            spaceType (str): The type of the space ('property').
            spaceColour (str): The colour group of the property.
            spacePrice (int): The price of the property.
        """
        super().__init__(spaceName, spaceType)
        self.spaceColour = spaceColour
        self.spacePrice = spacePrice
        self.owner = None


class Board(object):
    """
    Represents the game board consisting of various spaces like Go and Properties.
    """

    def __init__(self, spaceList=None):
        """
        Initializes a Board instance.

        Args:
            spaceList (list): A list of spaces on the board (default is an empty list).
        """
        if spaceList is None:
            self.spaceList = []
        else:
            self.spaceList = spaceList

    def ownerSameForColorOf(self, propertySpace):
        """
        Checks if all properties of the same colour group have the same owner.

        Args:
            propertySpace (Property): The property to check.

        Returns:
            bool: True if all properties of the same colour group have the same owner, 
                  False otherwise.
        """
        # Filter all properties on the board
        propertyList = [space for space in self.spaceList if isinstance(space, Property)]
        # Get all properties with the same colour group
        sameColorProperties = [p for p in propertyList if p.spaceColour == propertySpace.spaceColour]
        # Check if all properties in the colour group have the same owner
        ownerSameForColor = [p.owner == propertySpace.owner for p in sameColorProperties]
        return all(ownerSameForColor)

    @classmethod
    def fromJsonFile(cls, filename):
        """
        Creates a Board instance from a JSON file.

        Args:
            filename (str): Path to the JSON file containing board configuration.

        Returns:
            Board: A Board instance initialized with spaces from the JSON file.
        """
        # Load JSON data from the file
        with open(filename, 'r') as file:
            data = json.load(file)

        spaceList = []

        for spaceData in data:
            # Extract space type and name from the JSON data
            spaceType = spaceData.get("type")
            spaceName = spaceData.get("name")

            # Create a space based on its type
            if spaceType == "go":
                space = Go(spaceName=spaceName, spaceType=spaceType)
            elif spaceType == "property":
                space_price = spaceData.get("price", 0)
                space_colour = spaceData.get("colour", "None")
                space = Property(spaceName=spaceName, spaceType=spaceType, 
                                 spaceColour=space_colour, spacePrice=space_price)
            else:
                space = Space(spaceName=spaceName, spaceType=spaceType)

            # Add the space to the list
            spaceList.append(space)

        # Return a new Board instance initialized with the created spaces
        return Board(spaceList=spaceList)
