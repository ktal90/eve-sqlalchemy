from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import column_property, relationship

Base = declarative_base()


class CommonColumns(Base):
    __abstract__ = True
    _created = Column(DateTime, default=func.now())
    _updated = Column(DateTime, default=func.now(), onupdate=func.now())
    _etag = Column(String(40))
    ## if VERSIONING ##
    _version = Column(Integer)
    _latest_version = Column(Integer)


class PeopleColumns(object):
    id = Column(Integer, primary_key=True, autoincrement=True)
    firstname = Column(String(80))
    lastname = Column(String(120))

    @declared_attr
    def fullname(cls):
        return column_property(cls.firstname + " " + cls.lastname)


class People(CommonColumns, PeopleColumns):
    __tablename__ = 'people'


class Invoices(CommonColumns):
    __tablename__ = 'invoices'
    id = Column(Integer, primary_key=True, autoincrement=True)
    number = Column(Integer)
    people_id = Column(Integer, ForeignKey('people.id'))
    people = relationship(People, uselist=False)


class PeopleVersions(CommonColumns, PeopleColumns):
    __tablename__ = 'people_versions'
    id_document = Column(Integer, ForeignKey('people.id'), nullable=False)
