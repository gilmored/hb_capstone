from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Base = declarative_base()
class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)

def __init__(self, username, password):
    self.username = username
    self.password = password

engine = create_engine('sqlite:///users.db', echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# user1 = User(username='mike', password='pass123')
# session.add(user1)
# session.commit()


######################################

results = session.query(User).all()
print(results)