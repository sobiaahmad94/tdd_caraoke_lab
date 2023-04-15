import unittest

from src.guest import Guest
from src.song import *
from src.room import *

# from src.room import *

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Troy Barnes", 27)
        self.room_1 = Room("Room A", 50)
        self.room_2 = Room("Room B", 75)
        self.room_3 = Room("Room C", 100)

    def test_guest_has_name(self):
        self.assertEqual("Troy Barnes", self.guest.guest_has_name())
        # (expected, actual)
    
    def test_guest_has_age(self):
        self.assertEqual(27, self.guest.guest_has_age())
        # (expected, actual)
    
    def test_add_room(self):
        self.assertEqual(1, self.guest.add_room(room_1))


    #     self.room = Room("Room A") 
    #     self.room_list = []
    #     self.room_capacity = 50
    #     # this is a method, where I've created bar
    #     # whenever I use dot notation and refer to bar, it gives the name - "Karaoke Bar"
    # def test_room_has_name(self):
    #     self.assertEqual("Room A", self.room.room_name)