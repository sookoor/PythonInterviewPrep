import datetime

class Animal(object):
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, arrival_time = None):
        Animal.__init__(self, name)
        
        if arrival_time is None:
            self.arrival_time = datetime.datetime.now()
        else:
            self.arrival_time = arrival_time

class Cat(Animal):
    def __init__(self, name, arrival_time = None):
        Animal.__init__(self, name)

        if arrival_time is None:
            self.arrival_time = datetime.datetime.now()
        else:
            self.arrival_time = arrival_time

class AnimalShelter(object):
    def __init__(self):
        self.animal = [[], []] # [dog[], cat[]]
        
    def enqueue(self, animal):
        self.animal[type(animal) is Cat].insert(0, animal)

    def dequeueAny(self):

        # No dogs or cats
        if not self.animal[0] and not self.animal[1]:
            return None
        elif self.animal[0] and self.animal[1]:
            if self.animal[0][-1].arrival_time < self.animal[1][-1].arrival_time:
                return self.animal[0].pop()
            else:
                return self.animal[1].pop()
        else:
            return self.animal[self.animal[1]].pop()

    def dequeueDog(self):
        if self.animal[0]:
            return self.animal[0].pop()
        else:
            return None

    def dequeueCat(self):
        if self.animal[1]:
            return self.animal[1].pop()
        else:
            return None

if __name__ == "__main__":
    animals = [Dog("Snoopy"), Cat("Catbert"), Dog("Clifford"), Dog("Rex"), Cat("Jul")]

    animal_shelter = AnimalShelter()

    for animal in animals:
        animal_shelter.enqueue(animal)

    print "Should return Snoopy"
    print animal_shelter.dequeueAny().name

    print "Should return Clifford"
    print animal_shelter.dequeueDog().name

    print "Should return Catbert"
    print animal_shelter.dequeueCat().name
