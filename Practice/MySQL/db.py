from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker


# dialect+driver://username:password@host:port/database

# connect with data base
engine = create_engine("ENGINE_MYSQL_LOCALHOST_WITH_PORT", echo=True)
# manage tables
base = declarative_base()
#
# Session = sessionmaker(bind=engine)
# session = Session()


class Student(base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    # grade = Column(String)

    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age
        # self.grade = grade

    __tablename__ = 'backend'
    Re = Column(Integer, primary_key=True)
    de = Column(String)
    ge = Column(Integer)
    # grade = Column(String)

    def __init__(self, id, name, age):
        self.Re = Re
        self.de = de
        self.ge = ge
    # self.grade = grade


base.metadata.create_all(engine)
