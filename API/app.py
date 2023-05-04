from Server.instance import server
from marshmallow import ValidationError
from flask import jsonify

from db import db
from ma import ma 

from db import db
 
from controllers.book import Book, BookList

app = server.app
api = server.api




@app.before_first_request  # Creates the tables before the app gets run
def create_tables():
    db.create_all()


api.add_resource(Book, 'books/<int:id>') # Add the resource control on API
api.add_resource(BookList, 'books/')


if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    server.run()    


