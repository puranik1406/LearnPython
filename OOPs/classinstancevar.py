class Dog:
    species = "Canis familiaris"   # class variable

    def __init__(self, name, age):
        self.name = name           # instance variable
        self.age = age             # instance variable


dog1 = Dog("Buddy", 5)
dog2 = Dog("Lucy", 3)

print(dog1.species)  # ??
print(dog2.species)  # ??

Dog.species = "Canis lupus"        # changing class variable

print(dog1.species)  # ??
print(dog2.species)  # ??

dog1.species = "Golden Retriever"
print(dog1.species)   # ??
print(dog2.species)   # ??
