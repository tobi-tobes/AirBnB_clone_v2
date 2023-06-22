#!/usr/bin/python3
"""Tests for the Amenity Class """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
import os
import unittest


@unittest.skipUnless(os.getenv("HBNB_TYPE_STORAGE") != "db", "for db storage")
class test_Amenity(test_basemodel):
    """ amenity test class"""

    def __init__(self, *args, **kwargs):
        """inti the test class """
        super().__init__(*args, **kwargs)
        self.value = Amenity

    def test_name2(self):
        """testing name type """
        new_instance = self.value(name="Wifi")
        self.assertEqual(type(new_instance.name), str)
