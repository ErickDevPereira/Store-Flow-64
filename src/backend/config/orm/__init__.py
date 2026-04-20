from .settings import db, app

"""Explanation: These tables accomplish the relationship
one to many, where one user will be aligned to multiple connections 
while one connection is aligned with just one user."""

class Address(db.Model):

    __tablename__ = "address"

    #Columns
    addres_id = db.Column(db.Integer, primary_key = True)
    network_ip = db.Column(db.String(50), nullable = False, unique = True)
    blocked_status = db.Column(db.Integer, nullable = False) #1 means blocked, 0 means free
    #Relationship
    address_rl = db.relationship("NetworkConnection", back_populates = "net_rl")

class NetworkConnection(db.Model):

    __tablename__ = "network"

    #Columns
    id = db.Column(db.Integer, primary_key = True)
    address_id = db.Column(db.String(50), db.ForeignKey("address.addres_id"), nullable = False)
    logged_in = db.Column(db.Integer, nullable = False) #1 means logged in, 0 means logged out
    event_date = db.Column(db.DateTime, nullable = False)
    #Relationship
    net_rl = db.relationship("Address", back_populates = "address_rl")

with app.app_context():
    db.create_all() #Creating the database