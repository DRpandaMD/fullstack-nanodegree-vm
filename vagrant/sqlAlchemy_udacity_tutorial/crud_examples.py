# crud_create_example.py
# example to create items in the database

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine("sqlite:///restaurantmenu.db")
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# CRUD CREATE

# time to create entries in the database

myFirstRestaurant = Restaurant(name="Pizza Place")
session.add(myFirstRestaurant)
session.commit()

# now the data is in the database lets check it should return a hex memory value
session.query(Restaurant).all()

# now lets add an menu item to our restaurant
cheesepizza = MenuItem(name="Cheese Pizza", description="made with all natural ingredients and fresh mozzarella",
                       course="Entree", price="8.99", restaurant=myFirstRestaurant)
session.add(cheesepizza)
session.commit()
session.query(MenuItem).all()

# CRUD READ

firstResult = session.query(Restaurant).first()
print(firstResult.name)

items = session.query(MenuItem).all()
for item in items:
    print(item.name)

# CRUD UPDATE
# 1. Find entry
# 2. Reset Values
# 3. Add to Session
# 4. Call Session.commit()

veggieBurgers = session.query(MenuItem).filter_by(name='Veggie Burger')
for veggieBurger in veggieBurgers:
    print(veggieBurger.id)
    print(veggieBurger.price)
    print(veggieBurger.restaurant.name)
    print("\n")

# look for id of 8
UrbanVeggieBurger = session.query(MenuItem).filter_by(id=8).one()
print(UrbanVeggieBurger.price)
# after checking price we can set the price to new price
UrbanVeggieBurger.price = "2.99"
session.add(UrbanVeggieBurger)
session.commit()

# now to change ALL the veggie burger prices in the database
for veggieBurger in veggieBurgers:
    if veggieBurger.price != "2.99":
        veggieBurger.price = "2.99"
        session.add(veggieBurger)
        session.commit()


# CRUD DELETE
# 1. Find Entry
# 2. call session.delete(entry)
# 3. call session.commit()

spinach = session.query(MenuItem).filter_by(name="Spinach Ice Cream").one()
print(spinach.restaurant.name)
session.delete(spinach)
session.commit()
