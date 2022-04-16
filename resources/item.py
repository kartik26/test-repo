import sqlite3
from flask_restful import Resource,reqparse
from models.item import ItemModel
from flask_jwt import jwt_required
class Item (Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
            'price',
            type = float,
            required = True,
            help = "This filed can not be blank"
    )

    parser.add_argument(
            'store_id',
            type = int,
            required = True,
            help = "each item should have store_id"
    )
    #@jwt_required()
    def get (self,name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message' : 'Item not found'} , 404

    def post(self,name):
        if ItemModel.find_by_name(name):
            return{'message': "Item '{}'already exists".format(name)},400
        data = Item.parser.parse_args()
        item = ItemModel (name,data['price'],data['store_id'])
        try:
            #item.insert()
            item.save_to_db()

        except:
            return {'message' : 'there is error in inserting the item'} , 500 ###internal server error

        return item.json(),201  
    
    def delete(self,name):
        """"
        if ItemModel.find_by_name(name) is None:
            return{'message': "Item '{}'is not present".format(name)},400
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "DELETE FROM items WHERE name=?"
        cursor.execute(query,(name,))
        connection.commit()
        connection.close()
        """
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()

        return {'message' : 'Item deleted'}

    def put(self,name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        #updated_item = ItemModel(name, data['price'])
        if item is None:
            item = ItemModel(name , **data)
        else:
            item.price = data['price']  
        
        item.save_to_db()
        return item.json() 

class ItemList(Resource):
    def get(self):
        """"
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM items"
        result = cursor.execute(query)
        items = []
        for row in result:
            items.append({'name':row[0] , 'price' : row[1]})
        connection.close()
        return {'items' : items}
        """
        return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}#{'items' : [item.json() for item in ItemModel.query.all()]}