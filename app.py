"""Flask app for Cupcakes"""
import os

from flask import Flask, request, jsonify

from models import db, connect_db, Cupcake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", 'postgresql:///cupcakes')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

app.config['SECRET_KEY'] = "SECRET!"


@app.get('/api/cupcakes')
def get_all_cupcakes():
    """get all cupcakes"""

    cupcakes = Cupcake.query.all()
    serialized_cupcakes = [c.serialize() for c in cupcakes]

    return jsonify(cupcakes=serialized_cupcakes)


@app.get('/api/cupcakes/<int:cupcake_id>')
def get_cupcake(cupcake_id):
    """get cupcake"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized_cupcake = cupcake.serialize()

    return jsonify(cupcake=serialized_cupcake)


@app.post('/api/cupcakes')
def create_cupcake():
    """create cupcake"""

    flavor = request.json['flavor']
    size = request.json['size']
    rating = request.json['rating']
    image_url = request.json['image_url']

    new_cupcake = Cupcake(flavor=flavor,
                          size=size,
                          rating=rating,
                          image_url=image_url)

    db.session.add(new_cupcake)
    db.session.commit()

    serialized_new_cupcake = new_cupcake.serialize()

    return (jsonify(cupcake=serialized_new_cupcake), 201)
