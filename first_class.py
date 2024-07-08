class Person:
    def __init__(self):
        self.name = ""
        self.address = ""
        self.age = 0
        self.phone = ""

    def set_name(self, name):
        self.name = name

    def set_address(self, address):
        self.address = address

    def set_age(self, age):
        self.age = age

    def set_phone(self, phone):
        self.phone = phone

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_age(self):
        return self.age

    def get_phone(self):
        return self.phone


# Creating instances of the Person class
person1 = Person()
person1.set_name("Yaritza Islas")
person1.set_address("1122 main street, mchenry, illinois, 60097")
person1.set_age(25)
person1.set_phone("224-587-8702")

person2 = Person()
person2.set_name("Danny Covarrubias")
person2.set_address("456 Elm Street, mchenry, illinois, 60097")
person2.set_age(26)
person2.set_phone("888-555-5678")

person3 = Person()
person3.set_name("Bob Johnson")
person3.set_address("789 Oak Street, mchenry illinois")
person3.set_age(40)
person3.set_phone("122-555-9012")

# Displaying the information stored in each instance
print("Person 1:")
print("Name:", person1.get_name())
print("Address:", person1.get_address())
print("Age:", person1.get_age())
print("Phone:", person1.get_phone())
print()

print("Person 2:")
print("Name:", person2.get_name())
print("Address:", person2.get_address())
print("Age:", person2.get_age())
print("Phone:", person2.get_phone())
print()

print("Person 3:")
print("Name:", person3.get_name())
print("Address:", person3.get_address())
print("Age:", person3.get_age())
print("Phone:", person3.get_phone())
