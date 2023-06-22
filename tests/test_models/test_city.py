#!/usr/bin/python3
"""Tests for the City Class """
from tests.test_models.test_base_model import test_basemodel
from models.city import City
import os
import unittest


@unittest.skipUnless(os.getenv("HBNB_TYPE_STORAGE") != "db", "for db storage")
class test_City(test_basemodel):
    """ tests for city """

    def __init__(self, *args, **kwargs):
        """ init the test class"""
        super().__init__(*args, **kwargs)
        self.value = City

    def test_state_id(self):
        """ testing state_id type """
        new_instance = self.value(state_id="00003")
        self.assertEqual(type(new_instance.state_id), str)

    def test_name(self):
        """ testing name type"""
        new_instance = self.value(name="Dubai")
        self.assertEqual(type(new_instance.name), str)
