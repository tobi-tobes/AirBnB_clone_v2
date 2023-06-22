#!/usr/bin/python3
"""Tests for the User Class """
from tests.test_models.test_base_model import test_basemodel
from models.user import User
import os
import unittest

@unittest.skipUnless(os.getenv("HBNB_TYPE_STORAGE") == "db", "for db storage")
class test_User(test_basemodel):
    """ test class for user model"""

    def __init__(self, *args, **kwargs):
        """ user test class init"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ testing user first anme attr"""
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ testing user last name attr"""
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ testing user email attr"""
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ testing user password attr"""
        new = self.value()
        self.assertEqual(type(new.password), str)
