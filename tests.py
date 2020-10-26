from unittest import TestCase
from unittest.mock import patch
from random import random, randint

import main


class RoomAreaTest(TestCase):
    """
    This class contain tests for the RoomArea program.
    """
    def test_sample(self):
        """This test verifies that the output matches the sample run."""
        answer = main.room_area(11.0,2.0,4.0,7.0,1.0)
        self.assertEqual(answer, 53.5, "Incorrect value returned for float inputs.")

    def test_integers(self):
        """This test verifies that even when integers are inputted, the final result is a float."""
        answer = main.room_area(11,2,4,7,1)
        self.assertEqual(answer, 53.5, "Incorrect value returned for integer inputs. Make sure your final result is a float.")      
    
    def test_zero(self):
        """This test verifies the case of all 0 measurements."""
        answer = main.room_area(0,0,0,0,0)
        self.assertEqual(answer, 0.0, "Does not return 0 for measurements of 0")
    
    def test_random(self):
        """This test tests a random set of values."""
        a,b,c,d,e = [round(random()*randint(1,50),2) for x in range(5)]
        self.assertAlmostEqual(a*d-0.5*a*e+b*c-c*d+0.5*c*e, main.room_area(a,b,c,d,e),2,"Random values failed the test: {}".format([a,b,c,d,e]))