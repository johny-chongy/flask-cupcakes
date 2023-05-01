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
    """Return all cupcakes in JSON {'cupcakes': [{flavor, size, rating, image_url},...]}""" #FIXME: what does it do? what does it return? describe returned data

    cupcakes = Cupcake.query.all()
    serialized_cupcakes = [c.serialize() for c in cupcakes]

    return jsonify(cupcakes=serialized_cupcakes)


@app.get('/api/cupcakes/<int:cupcake_id>')
def get_cupcake(cupcake_id):
    """Return a cupcake in JSON {'cupcake': {flavor, size, rating, image_url}""" #FIXME:

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized_cupcake = cupcake.serialize()

    return jsonify(cupcake=serialized_cupcake)


@app.post('/api/cupcakes')
def create_cupcake():
    """Create a cupcake in JSON {'cupcake': {flavor, size, rating, image_url}""" #FIXME:

    flavor = request.json['flavor']
    size = request.json['size']
    rating = request.json['rating']
    image_url = request.json['image_url'] or None

    new_cupcake = Cupcake(
        flavor=flavor,
        size=size,
        rating=rating,
        image_url=image_url)

    db.session.add(new_cupcake)
    db.session.commit()

    serialized_new_cupcake = new_cupcake.serialize()

    return (jsonify(cupcake=serialized_new_cupcake), 201)

@app.patch('/api/cupcakes/<int:cupcake_id>')
def update_cupcake(cupcake_id):
    """Update a cupcake in JSON {'cupcake': {flavor, size, rating, image_url}""" #FIXME: more specific

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    # cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.flavor = request.json['flavor']
    cupcake.size = request.json['size']
    cupcake.rating = request.json['rating']

    # if condition (if there's key: update with new image or default image, no key: no update)
    cupcake.image_url = request.json['image_url']

    db.session.commit()

    serialized_updated_cupcake = cupcake.serialize()

    return (jsonify(cupcake=serialized_updated_cupcake), 200) #TODO: 200 as default if no value

@app.delete('/api/cupcakes/<int:cupcake_id>')
def delete_cupcake(cupcake_id):
    """Delete a cupcake and returns JSON {deleted: [cupcake_id]} """

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(deleted= [cupcake_id])