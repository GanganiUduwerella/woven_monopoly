import unittest
from game.board import Board, Property, Go

class TestOwnerSameForColorOf(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        
        self.board.spaceList.append(Go(spaceName="GO", spaceType="go"))
        
        self.board.spaceList.append(Property(spaceName="Red1", spaceType="property", spaceColour="Red", spacePrice=2))
        self.board.spaceList.append(Property(spaceName="Red2", spaceType="property", spaceColour="Red", spacePrice=3))
        self.board.spaceList.append(Property(spaceName="Blue1", spaceType="property", spaceColour="Blue", spacePrice=4))
        self.board.spaceList.append(Property(spaceName="Blue2", spaceType="property", spaceColour="Blue", spacePrice=5))

    def test_all_properties_same_color_same_owner(self):
        for space in self.board.spaceList:
            if isinstance(space, Property) and space.spaceColour == "Red":
                space.owner = "Player1"
        
        red_property = self.board.spaceList[1]
        self.assertTrue(self.board.ownerSameForColorOf(red_property))

    def test_properties_same_color_different_owners(self):
        self.board.spaceList[1].owner = "Player1"
        self.board.spaceList[2].owner = "Player2"
        
        red_property = self.board.spaceList[1]
        self.assertFalse(self.board.ownerSameForColorOf(red_property))

    def test_properties_different_colors_same_owner(self):
        for space in self.board.spaceList:
            if isinstance(space, Property):
                space.owner = "Player1"
        
        blue_property = self.board.spaceList[3]
        self.assertTrue(self.board.ownerSameForColorOf(blue_property))
        
        red_property = self.board.spaceList[1]
        self.assertTrue(self.board.ownerSameForColorOf(red_property))

if __name__ == "__main__":
    unittest.main()
