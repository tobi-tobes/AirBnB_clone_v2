#!/usr/bin/python3
"""Tests for the State Class """
from tests.test_models.test_base_model import test_basemodel
from models.state import State
import os
import unittest


@unittest.skipUnless(os.getenv("HBNB_TYPE_STORAGE") != "db", "for db storage")
class test_state(test_basemodel):
    """ states test class"""

    def __init__(self, *args, **kwargs):
        """ state test class init"""
        super().__init__(*args, **kwargs)
        self.value = State

    def test_name3(self):
        """ testing state name attr"""
        new = self.value(name="Florida")
        self.assertEqual(type(new.name), str)
