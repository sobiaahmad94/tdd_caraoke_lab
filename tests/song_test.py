import unittest

from src.song import Song
from src.guest import *
from src.room import *

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Colors by Halsey", 4.09)

    def test_song_has_name(self):
        self.assertEqual("Colors by Halsey", self.song.song_has_name())
        # (expected, actual)
    
    def test_song_duration_is_float(self):
        self.assertEqual(4.09, self.song.song_duration_is_float())

    # checking if value is a float
    # I expect every number inputed for duration to be a float
    # use float() method
    # use round to convert it to 2 decimal places
    # create var called duration_float
    # then use round(duration_float, 2)

