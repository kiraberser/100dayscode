from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean

from random import choice

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

@app.route("/")
def home():
    return render_template("index.html")

# HTTP GET - Read Record
@app.route('/random', methods=['GET'])
def get_random_cafe():
    random_cafe = choice(Cafe.query.order_by(Cafe.name).all())
    
    cafe_dict = {}
    for column in Cafe.__table__.columns:
        cafe_dict[column.key] = getattr(random_cafe, column.key)
    return jsonify(cafe=cafe_dict)

@app.route("/all")
def get_all_cafes():
    result = db.session.execute(db.select(Cafe).order_by(Cafe.name))
    all_cafes = result.scalars().all()
    #This uses a List Comprehension but you could also split it into 3 lines.
    return jsonify(cafes={cafe.id: cafe.to_dict() for cafe in all_cafes})

@app.route('/search')
def get_one_cafe():
    get_location = request.args.get('loc')
    get_cafe = db.session.execute(db.select(Cafe).where(Cafe.location == get_location))
    all_cafes = get_cafe.scalars().all()
    if all_cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404
# HTTP POST - Create Record

@app.route('/add', methods=['POST'])
def add_cafe():
    def str_to_bool(value):
        if value.lower() in ['true', '1', 'yes']:
            return True
        elif value.lower() in ['fakse', '0', 'no']:
            return False
        return value
    post_cafe_data = {key: str_to_bool(value)  for key, value in request.form.items()}

    #diccionario desempaquetado 
    new_cafe = Cafe(**post_cafe_data)
    db.session.add(new_cafe)
    db.session.commit()
    print(post_cafe_data)
    if post_cafe_data:
        return jsonify(response={'succes': "Succesfully added the new cafe."})
    else:
        return jsonify(error={"Not Found": "Sorry, we can't add a cafe."}), 404
# HTTP PUT/PATCH - Update Record

@app.route('/update-price/<int:cafe_id>', methods=['PATCH'])
def uptade_cafe(cafe_id):
    get_cafe = db.get_or_404(Cafe, cafe_id)
    new_price = request.args.get('price')
    print(get_cafe)
    get_cafe.coffee_price = new_price
    db.session.commit()
    if new_price:
        return jsonify(response={'succes': "Succesfully updated the price."})
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database"}), 404

# HTTP DELETE - Delete Record
@app.route('/report-closed/<int:cafe_id>', methods=['DELETE'])
def delete_cafe(cafe_id):
    # Obtener el api_key desde los argumentos de la solicitud
    api_key = request.args.get('api-key')
    
    # Verificar si el api_key es válido
    if api_key != "TopSecretAPIKey":
        return jsonify(error={'Sorry': "Sorry, that's not allowed. Make sure you have the correct api_key"})
    
    # Intentar obtener el café de la base de datos
    try:
        get_cafe = db.get_or_404(Cafe, cafe_id)
    except Exception as e:
        return jsonify(error={"Not Found": f"Sorry, a cafe with that id was not found in the database. Error: {str(e)}"})

    # Si el café existe, proceder con la eliminación
    try:
        db.session.delete(get_cafe)
        db.session.commit()
        return jsonify(response={'success': "Successfully deleted the cafe."})
    except Exception as e:
        db.session.rollback()
        return jsonify(error={"Error": f"An error occurred while trying to delete the cafe: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True)
