from .settings import db, app

"""Explanation: These tables accomplish the relationship
one to many, where one user will be aligned to multiple connections 
while one connection is aligned with just one user."""

class NetworkConnection(db.Model):

    __tablename__ = "network"

    #Columns
    id = db.Column(db.Integer, primary_key = True)
    ip = db.Column(db.String(50), nullable = False)
    logged_in = db.Column(db.Integer, nullable = False) #1 means logged in, 0 means logged out
    event_date = db.Column(db.DateTime, nullable = False)
    #Relationship
    net_rl = db.relationship("LoggedUsers", back_populates = "users_rl")

class LoggedUsers(db.Model):

    __tablename__ = "users"

    #Columns
    user_id = db.Column(db.Integer, primary_key = True)
    network_id = db.Column(db.Integer, db.ForeignKey("network.id"), nullable = False)
    #Relationship
    users_rl = db.relationship("NetworkConnection", back_populates = "net_rl")

with app.app_context():
    db.create_all() #Creating the database