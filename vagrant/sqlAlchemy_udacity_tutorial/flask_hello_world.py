# a hello world app using Flask

from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem
app = Flask(__name__)

# from Crud_examples.py
engine = create_engine("sqlite:///restaurantmenu.db")
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/hello')
def HelloWorld():
    restaurant = session.query(Restaurant).first()
    print(restaurant)
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant.id).all()
    print(items)
    output = "test "
    for i in items:
        print("iteration")
        output += i.name
        output += "</br>"
    print(output)
    print("after return")
    return output

if __name__ == '__main__':
    app.debug == True
    app.run(host='0.0.0.0', port=5000)

