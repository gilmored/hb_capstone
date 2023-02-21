from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker
from argon2 import PasswordHasher



class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(255), unique=True, nullable=False)
    # password = Column(String(255), nullable=False)
    hashed_password = Column(String, nullable=False)

ph = PasswordHasher()

# Creates user   // currently stores password in plain text
def create_user():
    engine = create_engine('sqlite:///users.db', echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    username = input("Enter username: ")
    password = input("Enter password: ")
    hashed_password = ph.hash(password)
    # user = User(username=username, password=password, hashed_password=hashed_password)
    user = User(username=username, hashed_password=hashed_password)
    session.add(user)
    session.commit()
    print("User created successfully.")

#Test to query the database for all users
    results = session.query(User).all()
    for result in results:
        print(result.username, result.hashed_password)
create_user()



