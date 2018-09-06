from eve_sqlalchemy.config import DomainConfig, ResourceConfig
from eve_sqlalchemy.examples.simple.tables import (Invoices, People,
                                                   PeopleVersions)

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/ex_eve'
SQLALCHEMY_TRACK_MODIFICATIONS = False
RESOURCE_METHODS = ['GET', 'POST']
ITEM_METHODS = ['PUT', 'GET', 'PATCH']

# The following two lines will output the SQL statements executed by
# SQLAlchemy. This is useful while debugging and in development, but is turned
# off by default.
# --------
SQLALCHEMY_ECHO = True
# SQLALCHEMY_RECORD_QUERIES = True

# The default schema is generated using DomainConfig:
DOMAIN = DomainConfig({
    'people': ResourceConfig(People),
    'invoices': ResourceConfig(Invoices),
    'People_versions': ResourceConfig(PeopleVersions)
}).render()

VERSIONING = True

# But you can always customize it:
DOMAIN['people'].update({
    'item_title': 'person',
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,
    'resource_methods': ['GET', 'POST', 'DELETE']
})
