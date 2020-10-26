import unittest
from unittest.mock import patch

import solution as main


class RoomAreaTest(unittest.TestCase):

    # @patch('builtins.input', lambda *args: 'y')
    def test_sample(self):
        answer = main.room_area(11.0,2.0,4.0,7.0,1.0)
        self.assertEqual(answer, 53.5, "Incorrect value returned for float inputs.")

    def test_integers(self):
        answer = main.room_area(11,2,4,7,1)
        self.assertEqual(answer, 53.5, "Incorrect value returned for integer inputs. Make sure your final result is a float.")      
    
    def test_zero(self):
        answer = main.room_area(0,0,0,0,0)
        self.assertEqual(answer, 0.0, "Does not return 0 for measurements of 0")