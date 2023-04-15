import unittest

from src.room import Room
from src.song import *
from src.guest import *

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Room A", 100)
        self.song = Song("Colors by Halsey", 4.09)
        self.song_1 = Song("Colors by Halsey", 4.09)
        self.song_2 = Song("Lose Yourself by Eminem", 5.20)
        self.song_3 = Song("Bad Guy by Billie Eilish", 3.14)
        self.guest = Guest("Troy Barnes", 30)
        self.guest_1 = Guest("Troy Barnes", 30)
        self.guest_2 = Guest("Abed Nadir", 31)
        self.guest_3 = Guest("Annie Edison", 29)
        
    def test_room_has_name(self):
        self.assertEqual("Room A", self.room.room_has_name())
    # (expected, actual)
    
    def test_add_song(self):
        self.assertEqual(1, self.room.add_song(song_2))


    def test_check_in_guest(self):
        self.assertEqual(1, self.room.check_in_guest(guest_3))

    def test_check_out_guest(self):
        self.room.check_in_guest(self.guest_1) # adding guest_1 to guests list
        self.room.check_in_guest(self.guest_2) # adding guest_2 to guests list
        self.room.check_in_guest(self.guest_3) # adding guest_3 to guests list
        self.assertEqual(True, self.room.check_out_guest(self.guest_3))
        self.assertEqual(2, len(self.room.guests))