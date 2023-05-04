from flask import request
from flask_restplus import Resource, fields

from models.book import Bookmodel
from schemas.book import BookSchema

from Server.instance import server

book_ns = server.book_ns

book_schema = BookSchema()
book_list_schema = BookSchema(many=True)


item = book_ns.model('Book', {
    'title': fields.String(description='Book Title'),
    'pages': fields.Integer(default=0)
})


class Book(Resource):
    
    def get(self, id):
        book_data = Bookmodel.find_by_id(id)
        if book_data:
            return book_schema.dump(book_data), 200 # Serielizing the variable book_data to Python object
        else:
            return {
                'message': "Book not Found"
            }, 404
        

    @book_ns.expect(item)  # Declare the model of data(payload) that the request is waiting for
    def put(self, id):
        book_data = Bookmodel.find_by_id(id)
        book_json = request.get_json()

        book_data.title = book_json['title']
        book_data.pages = book_json['pages']

        book_data.save_to_db()

        return book_schema.dump(book_data), 201 
    

    def delete(self, id):
        book_data = Bookmodel.find_by_id(id)
        if book_data:
            book_data.delete_from_db()
            return '', 204
        return {'message': 'Book not found'}, 404
        
        



class BookList(Resource):

    def get(self):
        return book_list_schema.dump(Bookmodel.find_all()), 200
    


    @book_ns.expect(item)
    @book_ns.doc('Create an Item')
    def post(self):
        book_json = request.get_json()
        book_data = book_schema.load(book_json)

        Bookmodel.save_to_db(book_data)

        return book_schema.dump(book_data), 201  # dump serielize the database object to python object
