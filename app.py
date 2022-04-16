from flask import Flask
from flask_restful import Resource,Api
from flask_jwt import JWT,jwt_required
from security import authenticate , identity
from resources.user import UserRegister
from resources.item import Item,ItemList
from resources.store import Store, StoreList
from db import db
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)
app.security_key = 'Kartik'

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app,authenticate,identity) 
db.init_app(app)
#class student (Resource):
    #def get(self,name):
        #return {'student':name}

#api.add_resource(student,'/student/<string:name>')

api.add_resource(Store,'/store/<string:name>')
api.add_resource(StoreList,'/stores')
api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(UserRegister,'/register')
if __name__ == '__main__':
    app.run(port=5000,debug=True)

