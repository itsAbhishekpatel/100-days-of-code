# declare a class, named as user/ blueprint - 
# use PascalCase for class and snake_case for objects and there is camelCase
class User:
    def __init__(self,user_id,user_name) -> None:
        print("new user being created...")
        # self.id is an attribute which is associated with the class
        # Initiaze the variables/attributes of the objects (has)
        self.id = user_id
        self.name = user_name
        self.follower = 0 # attribute which assign default value when object is created
        self.following = 0

    """method which is always have self paramenter means so that it knows the object 
       that called it"""
    def follow (self,user):
        user.follower += 1
        self.following += 1

# creating object of User class 
user_1 = User(2,"john")

# addding attribute for the particular object 
# attributes are variable associated with objects
user_1.id = "101"
user_1.username = "abhishek"

user_2 = User(2,"Abhishek")

print(user_1.id,user_1.name,user_1.follower)
user_1.follow(user_2)

print(user_1.follower)
print(user_1.following)

print(user_2.follower)
print(user_2.following)
# how can I start the peace of information when i created objects 
# in order to do that we use something called constructor 
# which is a part of blurprint and allow what should happens when the object is created.
# intializing of object 
# so we use special function init function

# init function call everytime when you create an object of this class 
# there is self which is actual object which is being created 
"""when the object is created by calling the call the object pass itself as an argument 
and receing as a parameter called self in constructor to initialize object attributes. """

"""we can set defualt value"""
# self = object 