import db
from sqlalchemy.orm import sessionmaker
import random

# new session
Session = sessionmaker(bind=db.engine)
session = Session()

# adding random data
for t in range(10, 20):
    # randomly generating values:
    id = random.randint(0, 1000)
    age = random.randint(20, 50)
# creating a new object based on student info:
    tr = db.Student(t, id, age)
    session.add(tr)

# save changes in data base
session.commit()
