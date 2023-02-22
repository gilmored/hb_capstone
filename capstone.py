from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker
from argon2 import PasswordHasher
import sys


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
    engine = create_engine('sqlite:///users.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    username = input("Enter username: ")
    password = input("Enter password: ")
    hashed_password = ph.hash(password)
    # password_hash = get_password_hash(password)
    user = User(username=username, hashed_password=hashed_password)
    # user = User(username=username, password=password, hashed_password=hashed_password)
    try:
        session.add(user)
        session.commit()
        print("#" * 25 + "\nUser created successfully.")
    except Exception:
        print("#" * 25 + "\nDuplicate username found. Enter a unique username.")
    


#Test to query the database for all users
    # results = session.query(User).all()
    # for result in results:
    #     print(result.username, result.hashed_password)

def login_user():
    engine = create_engine('sqlite:///users.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    username = input("Enter username: ")
    password = input("Enter password: ")

    try:
        user = session.query(User).filter_by(username=username).first()
        ph.verify(user.hashed_password, password)
    except Exception:
        print("#" * 25 + "\nInvalid username or password.")
    else:
        print("#" * 25 + "\nLogin successful.")

def main():
    active = True
    while active == True:
        print("#" * 25)
        choice = input("Enter \n1 to create user \n2 to login \n3 to exit\n ")
        if choice == '1':
            create_user()
            continue
        elif choice == '2':
            login_user()
            continue
        elif choice == '3':
            print("#" * 25 + "\nGoodbye\n" + "#" * 25)
            active = False
            sys.exit(0)
            

main()


