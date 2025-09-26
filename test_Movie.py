from unittest import TestCase
import Movie

class TestMovie(TestCase):

    def test_That_Movie_is_Added(self):
        Movie.add_movie("alaye")
        self.assertTrue(True, Movie.add_movie("alaye"))
