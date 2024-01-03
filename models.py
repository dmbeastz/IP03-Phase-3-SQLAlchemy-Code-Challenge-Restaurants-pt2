#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, desc
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

engine = create_engine('sqlite:///Restaurants.db')

Base = declarative_base()


