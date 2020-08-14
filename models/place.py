#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Table, ForeignKey, Float
from sqlalchemy import *
from os import getenv
from models.review import Review
from sqlalchemy.orm import relationship
metadata = Base.metadata
place_amenity = Table('place_amenity', metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'), primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
    reviews = relationship("Review", backref="place", cascade="all, delete")
    amenities = relationship("Amenity", secondary=place_amenity,
                             viewonly=False)

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def reviews(self):
            """ get list of reviews"""

            from models import storage

            ll = storage.all(Review)
            return [v for k, v in ll.items() if v.place_id == self.id]

        @property
        def amenities(self):
            """ returns the list of Amenity instances based on the attribute
            amenity_ids that contains all Amenity.id linked to the Place
            """
            alist = []
            for amen in storage.all(Amenity).values():
                if amen.place.id == self.id:
                    alist.append(amen)
            return alist

        @amenities.setter
        def amenities(self, obj):
            """ handles append method for adding an Amenity.id to the attribute
            amenity_ids. This method should accept only Amenity object,
            otherwise, do nothing.
            """
            if type(obj) == Amenity:
                self.amenity_ids.append(obj.id)
