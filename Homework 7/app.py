import os

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

DEFAULT_DB = "postgresql://@127.0.0.1/AIoT"
ACTUAL_DB = os.environ.get("DATABASE_URL", DEFAULT_DB).replace(
    "postgres://", "postgresql://"
)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = ACTUAL_DB
db = SQLAlchemy(app)


class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)


class Light(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float)
    status = db.Column(db.Integer)
    time = db.Column(db.DateTime, nullable=False)
    address = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


@app.route("/")
def index():
    return render_template("map.html")


@app.route("/location")
def location():
    locations = Location.query.all()
    return jsonify([location.name for location in locations])


@app.route("/light/<location>")
def light(location):
    lights = Light.query.filter_by(address=location).all()
    return jsonify([light.as_dict() for light in lights])
