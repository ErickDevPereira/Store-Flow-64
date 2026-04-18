from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from src.backend.config.api_settings import api

#This script will be called in order to set SQLAlchemy and the sqlite database.
#The sqlite will be used for a single objective: implementation of rating limit.

app: Flask =  api.app
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///ratelimit.db" #Set the database as sqlite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #Avoids anoying warnings
db: SQLAlchemy = SQLAlchemy(app) #sqlalchemy instance