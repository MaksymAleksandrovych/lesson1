class Pet:

   def __init__(self, name, species):

       self.name = name

       self.species = species

       self.is_alive = True

       self.age = 0

   def grow(self):

       self.age += 1

cat = Pet("Кася", "кіт")

dog = Pet("Чарлік", "собака")

cat.grow()

dog.grow()

print(f"{cat.name} росте і йому вже {cat.age} роки")

print(f"{dog.name} росте і йому вже {dog.age} роки")

