from src.backend.config.api_settings import api

"""Explanation: These tables accomplish the relationship
one to many, where one user will be aligned to multiple connections 
while one connection is aligned with just one user."""

class Address(api.db.Model):

    __tablename__ = "address"

    #Columns
    address_id = api.db.Column(api.db.Integer, primary_key = True)
    network_ip = api.db.Column(api.db.String(50), nullable = False, unique = True)
    blocked_status = api.db.Column(api.db.Integer, nullable = False) #1 means blocked, 0 means free
    #Relationship
    address_rl = api.db.relationship("NetworkConnection", back_populates = "net_rl")

class NetworkConnection(api.db.Model):

    __tablename__ = "network"

    #Columns
    id = api.db.Column(api.db.Integer, primary_key = True)
    address_id = api.db.Column(api.db.String(50), api.db.ForeignKey("address.address_id"), nullable = False)
    logged_in = api.db.Column(api.db.Integer, nullable = False) #1 means logged in, 0 means logged out
    event_date = api.db.Column(api.db.DateTime, nullable = False)
    #Relationship
    net_rl = api.db.relationship("Address", back_populates = "address_rl")