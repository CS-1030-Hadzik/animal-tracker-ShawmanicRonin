from animal import Animal
from dog import Dog
if __name__ == "__main__":
    # TODO: Create an instance of the Animal class
    Generic = Animal('Generic', 'Unknown')
    # TODO: Print the Animal instance
    print(Generic)
    # TODO: Call the method to make a generic animal sound
    Animal.speak()

    # TODO: Create an instance of the Dog class
    Buddy = Dog('Buddy', 'Canine', 'Golden Retriever')
    # TODO: Print the Dog instance
    print(Buddy)
    # TODO: Call the method to make the dog-specific sound
    Dog.speak()
    # TODO print out all the animals
    all_animals = Animal.get_all_animals()
    for animal in all_animals:
        print(animal)