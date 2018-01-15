# database_setup.py
# a database set up python file to set up a database using SQLAlchemy
# Michael Zarate 12/11/2017

import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


# Lets sqlalchemy know these are special classes
Base = declarative_base()


# now we are going to declare our two classes for the two tables we are going to use in the db
class Restaurant(Base):
    __tablename__ = "restaurant"
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)


class MenuItem(Base):
    __tablename__ = "menu_item"
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    course = Column(String(250))
    description = Column(String(250))
    price = Column(String(8))
    restaurant_id = Column(Integer, ForeignKey("restaurant.id"))
    restaurant = relationship(Restaurant)

    # added this block to serialize our data and send JSON objects
    @property
    def serialize(self):
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'price': self.price,
            'course': self.course
        }

# insert at EOF #
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine)

