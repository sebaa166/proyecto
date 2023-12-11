from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Categoria (db.Model): 
  cat_id = db.Column(db.Integer, primary_key=True)
  cat_nom= db.Column(db.String(100))
  cat_desp= db.Column(db.String(100)) 
  
  def __init__(self,cat_nom,cat_desp):
     self.cat_nom = cat_nom
     self.cat_desp = cat_desp

with app.app_context():
   db.create_all()

class CategoriaSchema(ma.Schema):
   class Meta:
      fields = ('cat_id', 'cat_nom', 'cat_desp')

categoria_schema = CategoriaSchema()
categorias_schema = CategoriaSchema(many=True)

@app.route('/categoria', methods=['GET'])
def get_categorias():
   all_categorias = Categoria.query.all()
   result = categorias_schema.dump(all_categorias)
   return jsonify(result)

@app.route('/', methods=['GET'])
def index():
    return jsonify({'mensaje':'bienvenido....'})

@app.route('/categoria/<id>',methods=['GET'])
def get_cat_id(id):
   una_cat = Categoria.query.get(id)
   return categoria_schema.jsonify(una_cat)

@app.route('/categoria/<id>',methods=['POST'])
def insert_cat():
   cat_nom = request.json ['cat_nom']
   cat_desp = request.json ['cat_desp']
   nuevo_reg = Categoria(cat_nom, cat_desp)
   db.session.add(nuevo_reg)
   db.session.commit()
   return categoria_schema.jsonify(nuevo_reg)

if __name__=="__main__":
    app.run(debug=True)


