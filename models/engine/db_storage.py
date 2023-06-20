#!/usr/bin/python3
'''database storage engine'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.amenity import Amenity
from models.base_model import Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv

classes = [User, City, State, Place, Review, Amenity]


class DBStorage:
    '''database storage engine for mysql storage'''
    __engine = None
    __session = None

    def __init__(self):
        '''instantiate new dbstorage instance'''
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')
        self.__engine = create_engine(f'mysql+mysqldb://{user}:{pwd}@{host}/\
{db}', pool_pre_ping=True)

        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        '''query on the current db session all cls objects'''
        dct = {}
        if cls is None:
            for c in classes:
                objs = self.__session.query(c).all()
                if not objs:
                    continue
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    dct[key] = obj
        else:
            objs = self.__session.query(cls).all()
            if objs:
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    dct[key] = obj
        return dct

    def new(self, obj):
        '''adds the obj to the current db session'''
        self.__session.add(obj)

    def save(self):
        '''commit all changes of the current db session'''
        self.__session.commit()

    def delete(self, obj=None):
        ''' deletes from the current databse session the obj
            is it's not None
        '''
        if obj is not None:
            self.__session.query(type(obj)).filter(
                type(obj).id == obj.id).delete()

    def reload(self):
        '''reloads the database'''
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """closes the working SQLAlchemy session"""
        self.__session.close()
