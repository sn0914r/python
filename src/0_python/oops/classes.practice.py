"""
Class: Student
Fields: name, marks
methods: is_pass()  # return True if marks >= 40
"""
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_pass(self):
        return self.marks >= 40


student1 = Student("tigor", 40)
print(student1.is_pass())


"""
Class: Rectangle
Fields: length, breadth
methods: area, perimeter
"""
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

rectangle1 = Rectangle(20, 30)
print(rectangle1.area())
print(rectangle1.perimeter())


"""
Class: BankAccount
Fields: balance
methods: deposit(amount), withdraw(amount)
"""
class BankAccount:
    def __init__(self):
        self.balance=0
    
    def deposit(self, amount):
        self.balance+=amount
        return f"Total balance: {self.balance}"
    
    def withdraw(self, amount):
        self.balance-=amount
        return f"Total balance: {self.balance}"
    
    def print_balance(self):
        print(f"Total balance: {self.balance}")

ba1 = BankAccount()
ba1.deposit(1000)
ba1.withdraw(500)
ba1.print_balance()

"""
Class: User
Fields: name
methods: update_name
"""
class User:
    def __init__(self, name):
        self.name = name
    
    def update_name(self, name):
        self.name = name
    
    def print_name(self):
        print(f"User name is {self.name}")

user1 = User("bhaai")
user1.print_name()
user1.update_name("tigor")
user1.print_name()


"""
Class: Counter
Fields: count
method: increment(), decrement()
"""
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count+=1
        return self.count
    
    def decrement(self):
        self.count-=1
        return self.count
    
    def reset(self):
        self.count = 0
        return self.count

    def print_count(self):
        print(f"count: {self.count}")

counter1 = Counter()
counter1.increment()
counter1.increment()
counter1.increment()

counter1.print_count()

counter1.decrement()
counter1.print_count()

counter1.reset()
counter1.print_count()