from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)

# Creates user   // currently stores password in plain text
def create_user():
    engine = create_engine('sqlite:///users.db', echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    username = input("Enter username: ")
    password = input("Enter password: ")
    user = User(username=username, password=password)
    session.add(user)
    session.commit()
    print("User created successfully.")

#Test to query the database for all users
    # results = session.query(User).all()
    # for result in results:
    #     print(result.username, result.password)
create_user()



