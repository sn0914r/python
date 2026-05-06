"""
1. class
2. object
3. __init__ -> runs automatically when an object is created
4. self -> points the current object
5. methods -> Fns written inside class
"""


class User:
    def __init__(self, name, branch):
        # print("I run automatically, when an object is created\n")
        self.name = name
        self.branch = branch

    def print_details(self):
        print(f"name: {self.name}")
        print(f"branch: {self.branch}")

    def greet(self):
        print(f"Hello {self.name}")

user1 = User("Sivananda", "CSM")
user2 = User("Ramesh", "CSE")

user1.print_details()
user2.print_details()

user2.greet()
# User.greet(user2)