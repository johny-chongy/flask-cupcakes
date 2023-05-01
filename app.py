"""Flask app for Cupcakes"""
import os

from flask import Flask, request, jsonify, render_template

from models import db, connect_db, Cupcake, DEFAULT_IMAGE_URL

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", 'postgresql:///cupcakes')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

app.config['SECRET_KEY'] = "SECRET!"

@app.get('/')
def get_homepage():
    """Shows static homepage"""

    return render_template('home.html')


@app.get('/api/cupcakes')
def get_all_cupcakes():
    """Return all cupcakes in JSON {'cupcakes': [{flavor, size, rating, image_url},...]}"""

    cupcakes = Cupcake.query.all()
    serialized_cupcakes = [c.serialize() for c in cupcakes]

    return jsonify(cupcakes=serialized_cupcakes)


@app.get('/api/cupcakes/<int:cupcake_id>')
def get_cupcake(cupcake_id):
    """Return a cupcake in JSON {'cupcake': {flavor, size, rating, image_url}"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized_cupcake = cupcake.serialize()

    return jsonify(cupcake=serialized_cupcake)


@app.post('/api/cupcakes')
def create_cupcake():
    """Create a cupcake; return JSON with inputted fields
    {'cupcake': {flavor, size, rating, image_url}"""

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
    """Update a cupcake and return JSON with updated fields
    {'cupcake': {flavor, size, rating, image_url}"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.rating = request.json.get('rating', cupcake.rating)

    if request.json.get('image_url') == '':
        cupcake.image_url = DEFAULT_IMAGE_URL
    else:
        cupcake.image_url = request.json.get('image_url', cupcake.image_url)

    db.session.commit()

    serialized_updated_cupcake = cupcake.serialize()

    return jsonify(cupcake=serialized_updated_cupcake)

@app.delete('/api/cupcakes/<int:cupcake_id>')
def delete_cupcake(cupcake_id):
    """Delete a cupcake and returns JSON {deleted: [cupcake_id]} """

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(deleted= [cupcake_id])