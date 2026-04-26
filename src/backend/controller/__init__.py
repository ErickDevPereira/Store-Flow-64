from .store import Store
from .register import Register
from .login import Login
from src.backend.config.api_settings import api
from .entities_endpoints import *
from .bridge import Bridge
from typing import List, Tuple
from flask_restful import Resource

routes_reg: List[Tuple[Resource, str]] = [
    (Store, "/store"),
    (Register, "/register"),
    (Login, "/login"),
    (EndpointsSuppliers, "/store/suppliers"),
    (EndpointsCategories, "/store/categories"),
    (EndpointsProducts, "/store/products"),
    (EndpointsEmpolyees, "/store/employees"),
    (EndpointsCustomers, "/store/customers"),
    (Bridge, "/store_bridge")
    ]

for route in routes_reg:
    api.set_rscs(route[0], route[1])