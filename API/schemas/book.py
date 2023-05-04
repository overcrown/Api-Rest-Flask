from ma import ma 

from models.book import Bookmodel

# This class is responsible to serielize the SQL DATA

class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Bookmodel
        load_instance = True