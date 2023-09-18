import db
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=db.engine)
session = Session()

# All data
for s in session.query(db.Student).all():
    print(s.id, s.age)

print("*"*20)
print("info with age over 40:")

# selected data
for s in session.query(db.Student).filter(db.Student.age > 40):
    print(s.id, s.age)
