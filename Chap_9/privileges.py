#!/usr/bin/env python3.7

# JulianV
# Apr 9, 2020.
# Exercise 9-8
# A class with one attribute.

class User():
    def __init__(self, user_name, first_name, 
            last_name, email):
        # Initializing User Attributes.
        self.user_name = user_name
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def describe_user(self):
        # formatting user output.
        print("\nUser information:")
        print(f"\tUser: {self.user_name}")
        print(f"\tFirst Name: {self.first_name}")
        print(f"\tLast name: {self.last_name}")
        print(f"\tEmail: {self.email}")
    
class Admin(User):
    #Initializing Admin Attributes
    def __init__(self, user_name, first_name,
            last_name, email):
        super().__init__(user_name, first_name, 
            last_name, email)
        self.admin = True
        # This Attribute connects to Privilege Class.
        self.privileges = Privileges()

class Privileges():
    def __init__(self, privileges=[]):
        self.privileges = ['can add post', 'can delete post',
                        'can band user', 'can edit post',
                ]

    def show_privileges(self):
        # Display Admin privileges.
        print("Admin Privileges:")
        print(f"\t-Admin: {self.privileges}")
        for privilege in self.privileges:
            print(f"\t-{privilege}")




my_user = User('josev', 'jose', 'vargas', 'josev@example.com')
my_user.describe_user()

new_user = Admin('julianv', 'julian', 'vargas', 'julianv@example.com')
new_user.describe_user()

# Accessing Privilege class through 
# privilege attribute.
new_user.privileges.show_privileges()
