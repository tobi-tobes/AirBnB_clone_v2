#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class / table model"""
    __tablename__ = 'states'
    __table_args__ = ({'mysql_default_charset': 'latin1'})

    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state',
                          cascade='all, delete')

    @property
    def cities(self):
        '''returns the list of City instances with state_id
        equals the current State.id FileStorage relationship
        between State and City
        '''
        from models import storage
        from models.city import City

        related_cities = []
        cities = storage.all(City)
        for city in cities.values():
            if city.state_id == self.id:
                related_cities.append(city)
        return related_cities
