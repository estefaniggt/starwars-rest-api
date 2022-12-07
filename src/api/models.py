from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, foreignKey, Integer, String

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(120), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)

    def __init__(self, **kwargs):
        self.full_name = kwargs['full_name']
        self.email = kwargs['email']
        self.password = kwargs['password']

    @classmethod
    def create(cls, **kwargs):
        new_user = cls(**kwargs)
        db.session.add(new_user)

        try:
            db.session.commit()
            return new_user
        except Exception as error:
            raise Exception(error.args[0], 400)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "full_name": self.full_name,
            "email": self.email
            # do not serialize the password, its a security breach
        }

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    gender = db.Column(db.String(40))
    hair_color = db.Column(db.String(40))
    eye_color = db.Column(db.String(40))

    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.gender = kwargs['gender']
        self.hair_color = kwargs['hair_color']
        self.eye_color = kwargs['eye_color']

    @classmethod
    def create(cls, **kwargs):
        new_character = cls(**kwargs)
        db.session.add(new_character)

        try:
            db.session.commit()
            return new_character
        except Exception as error:
            raise Exception(error.args[0], 400)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "hair_color": self.hair_color,
            "eye_color": self.eye_color
        }

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    population = db.Column(db.String(120))
    terrain = db.Column(db.String(120))
    diameter = db.Column(db.String(120))

    def __init__(self, **kwargs):
        self.name = kwargs['name'],
        self.population = kwargs['population']
        self.terrain = kwargs['terrain']
        self.diameter = kwargs['diameter']

    @classmethod
    def create(cls, **kwargs):
        new_planet = cls(**kwargs)
        db.session.add(new_planet) 

        try:
            db.session.commit()
            return new_planet
        except Exception as error:
            raise Exception(error.args[0],400)
    
    def serialize(self):
        return {
            "id" : self.id, 
            "name" : self.name,
            "population" : self.population,
            "terrain" : self.terrain,
            "diameter" : self.diameter
        }

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    model = db.Column(db.String(120))
    passengers = db.Column(db.String(120))
    length = db.Column(db.String(120))

    def __init__(self, **kwargs):
        self.name = kwargs['name'],
        self.model = kwargs['model']
        self.passengers = kwargs['passengers']
        self.length = kwargs['length']
    
    @classmethod
    def create(cls, **kwargs):
        new_vehicle = cls(**kwargs)
        db.session.add(new_vehicle ) # INSERT INTO

        try:
            db.session.commit() # Se ejecuta el INSERT INTO
            return new_vehicle 
        except Exception as error:
            raise Exception(error.args[0],400)
    
    def serialize(self):
        return {
            "id" : self.id, 
            "name" : self.name,
            "model" : self.model,
            "passengers" : self.passengers, 
            "length" : self.length
        }

class Character_Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)   
    name = db.Column(db.String(200), nullable=False)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'))
    user_id = db.Column(db.Integer, db.ForeignKey ('user.id'))

    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.character_id = kwargs['character_id']
        self.user_id = kwargs['user_id']

    @classmethod
    def create(cls, **kwargs):
        new_character_favorite = cls(**kwargs)
        db.session.add(new_character_favorite)

        try:
            db.session.commit()
            return new_character_favorite
        except Exception as error:
            raise Exception(error.args[0], 400)

    def serialize(self):
        return {
            "name": self.name,
            "character_id": self.character_id,
            "user_id": self.user_id
        }    

class Planet_Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(200), nullable=False)
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))
    user_id = db.Column(db.Integer, db.ForeignKey ('user.id'))

    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.planet_id = kwargs['planet_id']
        self.user_id = kwargs['user_id']
        
    @classmethod
    def create(cls, **kwargs):
        new_planet_favorite = cls(**kwargs)
        db.session.add(new_planet_favorite)

        try:
            db.session.commit()
            return new_character_favorite
        except Exception as error:
            raise Exception(error.args[0], 400)

    def serialize(self):
        return {
            "name": self.name,
            "planet_id": self.planet_id,
            "user_id": self.user_id
        } 

class Vehicle_Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(200), nullable=False)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'))
    user_id = db.Column(db.Integer, db.ForeignKey ('user.id'))

    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.vehicle_id = kwargs['vehicle_id']
        self.user_id = kwargs['user_id']
        
    @classmethod
    def create(cls, **kwargs):
        new_vehicle_favorite = cls(**kwargs)
        db.session.add(new_vehicle_favorite)

        try:
            db.session.commit()
            return new_vehicle_favorite
        except Exception as error:
            raise Exception(error.args[0], 400)

    def serialize(self):
        return {
            "name": self.name,
            "vehicle_id": self.vehicle_id,
            "user_id": self.user_id
        } 