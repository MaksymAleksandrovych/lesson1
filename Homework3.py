class Pet:

   def __init__(self, name="Charlik", year=1, breed="Yorkshire"):
       self.name = name
       self.yaer = year
       self.breed = breed
       self.status = "available"


class Homes:

   def __init__(self):

       self.pet = []


   def add_puppy(self, pet):

       self.pet.append(pet)

