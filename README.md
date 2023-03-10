# User authentication exercise

This is a simple user authentication system that allows users to create an account and login. It uses the argon2 library to hash passwords and stores user data in an SQLite database.

## Goals

This exercise allows a user to create an account by supplying a username and password. The password is salted and then hashed using Argon2 and stored in an SQLite database using SQLAlchemy. The user can then login by supplying their login credentials. 

## Walkthrough

Getting into the project. Upon starting, the user is given the choice of creating a new user, signing in, or exiting the program. 

If the user selects to create a new user, they’ll be prompted to to enter a username and password. Guardrails such as needing uppercase and lowercase letters, a number, special character, and at least eight characters, have been added to guide the user in creating a password. Once the user has entered an acceptable new username and password, salt is added to the password and the password is then hashed using Argon2’s hashing function. The information is then stored in a database. 

If the user selects to sign in, the user will be prompted to enter their credentials. If the credentials pass validation, they’re given a successful login message. Otherwise, the login fails. As I created this program as a learning experience, it runs on a loop until the user exits the program. 

![gif walkthrough of usage](/cap_scratch/walkthrough.gif)