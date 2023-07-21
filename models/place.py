#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship

place_amenity = Table('place_amenity', Base.metadata,
                Column("place_id", String(60), ForeignKey('places.id'),
                       nullable=False, primary_key=True),
                Column("amenity_id", String(60), ForeignKey('amenities.id'),
                       nullable=False, primary_key=True),
                mysql_charset="latin1"
                )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    __table_args__ = ({'mysql_default_charset': 'latin1'})

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship('Review', cascade="all, delete, delete-orphan",
                           backref="place")
    amenities = relationship('Amenity', secondary="place_amenity",
                             viewonly=False)

    @property
    def reviews(self):
        '''returns the list of Review instances with place_id
        equals the current place.id
        '''
        from models import storage
        related_reviews = []
        reviews = storage.all(Review)
        for review in reviews.values():
            if review.place_id == self.id:
                related_reviews.append(review)
        return related_reviews

    @property
    def amenities(self):
        '''returns the list of Amenity instances with place_id
        equals the current place.id
        '''
        return self.amenity_ids

    @amenities.setter
    def amenities(self, amenity):
        """handles append method for adding an Amenity.id
        to the attribute amenity_ids"""
        if type(amenity).__name__ == "Amenity":
            self.amenity_ids.append(amenity.id)
