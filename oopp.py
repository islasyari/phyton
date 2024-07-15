class Pet:
    vet_name = "Your Veterinary Office"

    def __init__(self, owner_first_name, owner_last_name, pet_id, pet_name, pet_type="Dog"):
        self.__owner_first_name = owner_first_name
        self.__owner_last_name = owner_last_name
        self.__pet_id = pet_id
        self.__pet_name = pet_name
        self.__pet_type = pet_type

    def get_owner_first_name(self):
        return self.__owner_first_name

    def set_owner_first_name(self, owner_first_name):
        self.__owner_first_name = owner_first_name

    def get_owner_last_name(self):
        return self.__owner_last_name

    def set_owner_last_name(self, owner_last_name):
        self.__owner_last_name = owner_last_name

    def get_pet_id(self):
        return self.__pet_id

    def set_pet_id(self, pet_id):
        self.__pet_id = pet_id

    def get_pet_name(self):
        return self.__pet_name

    def set_pet_name(self, pet_name):
        self.__pet_name = pet_name

    def get_pet_type(self):
        return self.__pet_type

    def set_pet_type(self, pet_type):
        self.__pet_type = pet_type

    def display_pet_info(self):
        print("Pet Information:")
        print(f"Owner: {self.get_owner_first_name()} {self.get_owner_last_name()}")
        print(f"Pet ID: {self.get_pet_id()}")
        print(f"Pet Name: {self.get_pet_name()}")
        print(f"Pet Type: {self.get_pet_type()}")
        print(f"Veterinary Office: {Pet.vet_name}")



# Creating the pet list
pet1 = Pet("yaritza", "islas", 1, "Max", "Dog")
pet2 = Pet("chris", "evans", 2, "Bella", "Cat")
pet3 = Pet("Michael", "Jackson", 3, "Charlie")

# Using setter method
pet1.set_pet_type("Fish")

# Display pet information
pet1.display_pet_info()
print()
pet2.display_pet_info()
print()
pet3.display_pet_info()

def check_property(pet, property_name):
    return hasattr(pet, property_name)

# Check the results
print(check_property(pet1, "pet_type"))
print(check_property(pet2, "owner_first_name"))
print(check_property(pet3, "age"))



