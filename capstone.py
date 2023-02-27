from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker
from argon2 import PasswordHasher
import sys
import re


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(255), unique=True, nullable=False)
    # password = Column(String(255), nullable=False)
    hashed_password = Column(String, nullable=False)

ph = PasswordHasher()

def create_user():
    engine = create_engine('sqlite:///users.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    while True:
        username = input("Enter username: ")
        if len(username) < 1:
            print("#" * 25 + "\nUsername cannot be empty.")
            continue
        existing_user = session.query(User).filter(User.username == username).first()
        if existing_user is not None:
            print("#" * 25 + "\nUsername already exists.")
            continue
        break
    while True:
        password = input("Enter password: ")
        if len(password) < 8:
            print("#" * 25 + "\nPassword must be at least 8 characters.")
            continue
        if not re.search("[A-Z]", password):
            print("#" * 25 + "\nPassword must contain at least one uppercase letter.")
            continue
        if not re.search("[a-z]", password):
            print("#" * 25 + "\nPassword must contain at least one lowercase letter.")
            continue
        if not re.search("[0-9]", password):
            print("#" * 25 + "\nPassword must contain at least one number.")
            continue
        if not re.search("[!@#$%^&*(),.?:{}|<>]", password):
            print("#" * 25 + "\nPassword must contain at least one special character.")
            continue
        break
    
    hashed_password = ph.hash(password)
    user = User(username=username, hashed_password=hashed_password)

    session.add(user)
    session.commit()
    print("#" * 25 + "\nUser created successfully.")
    

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


