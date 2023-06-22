#!/usr/bin/python3
"""Tests for the Place Class """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
import os
import unittest


@unittest.skipUnless(os.getenv("HBNB_TYPE_STORAGE") != "db", "for db storage")
class test_Place(test_basemodel):
    """ place tests class"""

    def __init__(self, *args, **kwargs):
        """ init test class"""
        super().__init__(*args, **kwargs)
        self.value = Place

    def test_city_id(self):
        """ testing place city_id attr"""
        new = self.value(city_id="0897-6543")
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ testing place user_id attr"""
        new = self.value(user_id="57634")
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ testing place name attr"""
        new = self.value(name="My little house")
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """testing place description attr"""
        new = self.value(description="")
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ testing place number of rooms attr"""
        new = self.value(number_rooms=2)
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ testing place number of bathrooms attr"""
        new = self.value(number_bathrooms=1)
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ testing place max_guest attr"""
        new = self.value(max_guest=3)
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ testing place price by night attr"""
        new = self.value(price_by_night=85)
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ testing place latitud attr"""
        new = self.value(latitude=23.56874)
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ testing place longitude attr"""
        new = self.value(longitude=-32.1114)
        self.assertEqual(type(new.longitude), float)

    @unittest.expectedFailure
    def test_amenity_ids(self):
        """ testing amenity ids"""
        new = self.value(amenity_ids)
        self.assertTrue(hasattr(new, amenity_ids))
