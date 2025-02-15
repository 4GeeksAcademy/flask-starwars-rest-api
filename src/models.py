from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    def __repr__(self):
        return '<User %r>' % self.id
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "is_active": self.is_active,
            # do not serialize the password, its a security breach
        }
    
class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey('user.id'))
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'))
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'))
    def __repr__(self):
        return '<Favorite %r>' % self.id
    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.userid,
            "character_id": self.characterid,
            "planet_id": self.planet_id,
            "vehicle_id": self.vehicle_id
        }
    
class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    height = db.Column(db.Integer)
    mass = db.Column(db.Integer)
    hair_color = db.Column(db.String(50))
    skin_color = db.Column(db.String(50))
    eye_color = db.Column(db.String(50))
    birth_year = db.Column(db.String(50))
    gender = db.Column(db.String(10))
    like = db.Column(db.Boolean)
    favorite = db.relationship('Favorite', backref='character', lazy=True)
    def __repr__(self):
        return '<Character %r>' % self.id
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "like": self.like,
            "favorite": self.favorite
        }


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    rotation_period = db.Column(db.Integer)
    orbital_period = db.Column(db.Integer)
    diameter = db.Column(db.Integer)
    climate = db.Column(db.String(100))
    gravity = db.Column(db.String(50))
    terrain = db.Column(db.String(100))
    surface_water = db.Column(db.Integer)
    population = db.Column(db.Integer)
    like = db.Column(db.Boolean)
    favorite = db.relationship('Favorite', backref='planet', lazy=True)
    def __repr__(self):
        return '<Planet %r>' % self.id
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "diameter": self.diameter,
            "climate": self.climate,
            "gravity": self.gravity,
            "terrain": self.terrain,
            "surface_water": self.surface_water,
            "population": self.population,
            "like": self.like,
            "favorite": self.favorite,
        }

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    manufacturer = db.Column(db.String(50), nullable=False)
    cost_in_credits = db.Column(db.Integer, nullable=False)
    length = db.Column(db.Float, nullable=False)
    max_atmosphering_speed = db.Column(db.Integer, nullable=False)
    crew = db.Column(db.Integer, nullable=False)
    passengers = db.Column(db.Integer)
    cargo_capacity = db.Column(db.Integer)
    consumables = db.Column(db.String(50))
    vehicle_class = db.Column(db.String(50))
    like = db.Column(db.Boolean)
    favorite = db.relationship('Favorite', backref='vehicle', lazy=True)
    def __repr__(self):
        return '<Vehicle %r>' % self.id
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "cost_in_credits": self.cost_in_credits,
            "length": self.length,
            "max_atmosphering_speed": self.max_atmosphering_speed,
            "crew": self.crew,
            "passengers": self.passengers,
            "cargo_capacitiy": self.cargo_capacity,
            "consumables": self.consumables,
            "vehicle_class": self.vehicle_class,
            "like": self.like,
            "favorite": self.favorite
        }