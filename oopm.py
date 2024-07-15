class Pet:
    def __init__(self, kind, breed, name):
        self.kind = kind
        self.breed = breed
        self.name = name

    def get_kind(self):
        return self.kind

    def set_kind(self, kind):
        self.kind = kind

    def get_breed(self):
        return self.breed

    def set_breed(self, breed):
        self.breed = breed

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def print_details(self):
        print(f"Kind: {self.kind}")
        print(f"Breed: {self.breed}")
        print(f"Name: {self.name}")


# Create instances of the Pet class
pet1 = Pet("dog", "Labrador Retriever", "Max")
pet2 = Pet("cat", "Siamese", "Luna")
pet3 = Pet("bird", "Parakeet", "Charlie")

# Call the print_details method for each pet
pet1.print_details()
pet2.print_details()
pet3.print_details()

# Demonstrate the use of the type() function
print(type(pet1))  # Output: <class '__main__.Pet'>


