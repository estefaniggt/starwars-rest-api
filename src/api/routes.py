"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Character, Planet, Vehicle, Character_Favorite, Planet_Favorite, Vehicle_Favorite
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)

@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

@api.route('/users', methods=['POST', 'GET'])
def get_users():
    if request_method == 'GET':
        users = User.query.all()
        users_dictionaries = []

        for user in users:
            users_dictionaries.append(user.serialize())

        return jsonify(users_dictionaries), 200
    
    new_user_data = request.json

    try:
        new_user = User.create(**new_user_data)
        return jsonify(new_user.serialize()),201
    except Exception as error:
        return jsonify(error.args[0], error.args[1] if len(error.args) > 1 else 500)

@api.route('/people', methods=['GET','POST'])
def get_characters():
    if request.method == 'GET':
        characters = Character.query.all()
        characters_dictionaries = []

        for character in characters:
            characters_dictionaries.append(character.serialize())

        return jsonify(characters_dictionaries)

    new_character_data = request.json

    try:
        new_character = Character.create(**new_character_data)
        return jsonify(new_character.serialize()),201
    except Exception as error:
        return jsonify(error.args[0], error.args[1] if len(error.args) > 1 else 500)

@api.route('/planets', methods=['GET','POST'])
def get_planets():
    if request.method == 'GET':
        planets = Planet.query.all()
        planets_dictionaries = []

        for planet in planets:
            planets_dictionaries.append(planet.serialize())
        
        return jsonify(planets_dictionaries)
    
    new_planet_data = request.json

    try:
        new_planet = Planet.create(**new_planet_data)
        return jsonify(new_planet.serialize()),201
    except Exception as error:
        return jsonify(error.args[0], error.args[1] if len(error.args) > 1 else 500)

@api.route('/vehicles', methods=['GET','POST'])
def get_vehicles():
    if request.method == 'GET':
        vehicles = Vehicle.query.all()
        vehicles_dictionaries = []

        for vehicle in vehicles:
            vehicles_dictionaries.append(vehicle.serialize())
        
        return jsonify(vehicles_dictionaries)
    
    new_vehicle_data = request.json

    try:
        new_vehicle = Vehicle.create(**new_vehicle_data)
        return jsonify(new_vehicle.serialize()),201
    except Exception as error:
        return jsonify(error.args[0], error.args[1] if len(error.args) > 1 else 500)

@api.route('/users/<int:user_id>/favorites', methods=['GET'])
def get_favorites(user_id):
    if request.method == 'GET':
        characters_favorite = Character_Favorites.query.filter_by(user_id = user_id).all()
        planets_favorite = Planet_Favorites.query.filter_by(user_id = user_id).all()
        vehicle_favorite = Vehicle_Favorites.query.filter_by(user_id = user_id).all()

        favorites_dictionaries = []

        for character_favorite in characters_favorite:
            favorites_dictionaries.append(character_favorite.serialize())
        for planet_favorite in planets_favorite:
            favorites_dictionaries.append(planet_favorite.serialize())
        for vehicle_favorite in vehicles_favorite:
            favorites_dictionaries.append(vehicle_favorite.serialize())

        return jsonify(favorites_dictionaries)

@api.route('/favorite/people/<int:user_id>/<int:people_id>', methods=['POST'])
def add_character_in_favorites(user_id, people_id):
        new_people_favorite_data = request.json

        favorites = Favorite.query.filter_by(user_id = user_id, character_id = people_id).first()
        if favorites is not None:
            return jsonify({"msg": "The character is already loaded in the favorites"}), 401
            else:
                try:
                    new_favorite = Favorite.create_favorite(user_id = user_id, character_id = people_id, **new_favorite_data)
                    return jsonify(new_favorite.serialize()),201
                except Exception as error:
                    return jsonify(error.args[0], error.args[1] if len(error.args) > 1 else 500)

@api.route('/favorite/people/<int:user_id>/<int:people_id>', methods=['DELETE'])
def delete_character_in_favorite(people_id,user_id):
    remove_favorite = Favorite.query.filter_by(user_id = user_id, character_id = people_id).first()
    try:
        remv_favorite = Favorite.favorite_remv(remove_favorite)
        return jsonify(remv_favorite),200
    except Exception as error:
        return jsonify(error.args[0], error.args[1] if len(error.args) > 1 else 500) 

@api.route('/favorite/planet/<int:user_id>/<int:planet_id>', methods=['POST'])
def add_planet_in_favorites(planet_id,user_id):
    new_planet_favorite_data = request.json

    favorites = Favorite.query.filter_by(user_id = user_id, planet_id = planet_id).first()
    if favorites is not None:
        return jsonify({"msg": "The planet is already loaded in the favorites"}), 401
    else:
        try:
            new_favorite = Favorite.create_favorite(user_id = user_id, planet_id = planet_id, **new_favorite_data)
            return jsonify(new_favorite.serialize()),201
        except Exception as error:
            return jsonify(error.args[0], error.args[1] if len(error.args) > 1 else 500)

@api.route('/favorite/planet/<int:user_id>/<int:planet_id>', methods=['DELETE'])
def delete_planet_to_favorite(planet_id,user_id):
    remove_favorite = Favorite.query.filter_by(user_id = user_id, planet_id = planet_id).first()
    try:
        remv_favorite = Favorite.favorite_remv(remove_favorite)
        return jsonify(remv_favorite),200
    except Exception as error:
        return jsonify(error.args[0], error.args[1] if len(error.args) > 1 else 500)

@api.route('/favorite/vehicle/<int:user_id>/<int:vehicle_id>', methods=['POST'])
def add_vehicle_in_favorite(vehicle_id,user_id):
        new_vehicle_favorite_data = request.json

        favorites = Favorite.query.filter_by(user_id = user_id, vehicle_id = vehicle_id).first()
        if favorites is not None:
            return jsonify({"msg": "The vehicle is already loaded in the favorites"}), 401
        else:
            try:
                new_favorite = Favorite.create_favorite(user_id = user_id, vehicle_id = vehicle_id, **new_favorite_data)
                return jsonify(new_favorite.serialize()),201
            except Exception as error:
                return jsonify(error.args[0], error.args[1] if len(error.args) > 1 else 500)

@api.route('/favorite/vehicle/<int:user_id>/<int:vehicle_id>', methods=['DELETE'])
def delete_vehicle_to_favorite(vehicle_id,user_id):
    remove_favorite = Favorite.query.filter_by(user_id = user_id, vehicle_id = vehicle_id)[0]
    try:
        remv_favorite = Favorite.favorite_remv(remove_favorite)
        return jsonify(remv_favorite),200
    except Exception as error:
        return jsonify(error.args[0], error.args[1] if len(error.args) > 1 else 500) 