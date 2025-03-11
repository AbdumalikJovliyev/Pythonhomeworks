# ## Model a Farm

# In this assignment, you’ll create a simplified model of a farm. As you work through this assignment, keep in mind that there are a number of correct answers.

# The focus of this assignment is less about the Python class syntax and more about software design in general, which is highly subjective. This assignment is intentionally left open-ended to encourage you to think about how you would organize your code into classes.

# Before you write any code, grab a pen and paper and sketch out a model of your farm, identifying classes, attributes, and methods. Think about inheritance. How can you prevent code duplication? Take the time to work through as many iterations as you feel are
# necessary.

# The actual requirements are open to interpretation, but try to adhere to these guidelines:

# 1. You should have at least four classes: the parent `Animal` class, and then at least three child animal classes that inherit from Animal.
# 2. Each class should have a few attributes and at least one method that models some behavior appropriate for a specific animal or all animals—such as walking, running, eating, sleeping, and so on.
# 3. Keep it simple. Utilize inheritance. Make sure you output details about the animals and their behaviors.


# Parent Class: Animal
class Animal:
    def __init__(self, name, age, sound):
        self._name = name
        self._age = age
        self._sound = sound
        self._health = 100  # Default health

    # Property for name
    @property
    def name(self):
        return self._name

    # Property for age
    @property
    def age(self):
        return self._age

    # Property for health
    @property
    def health(self):
        return self._health

    # Method to make sound
    def make_sound(self):
        print(f"{self._name} says: {self._sound}")

    # Method to eat (restores health)
    def eat(self, food):
        print(f"{self._name} is eating {food}.")
        self._health = min(self._health + 20, 100)  # Increase health by 20 but max 100

    # Method to decrease health
    def reduce_health(self, amount):
        self._health = max(self._health - amount, 0)  # Reduce health but min 0

    # Method to display animal info
    def display_info(self):
        print(f"Name: {self._name}, Age: {self._age}, Health: {self._health}")

# Child Class: Cow
class Cow(Animal):
    def __init__(self, name, age, milk_production):
        super().__init__(name, age, "Moo")
        self._milk_production = milk_production

    def produce_milk(self):
        if self.health > 30:
            print(f"{self.name} produces {self._milk_production} liters of milk daily.")
            self.reduce_health(15)  # Reduce health by 15
        else:
            print(f"{self.name} is too weak to produce milk!")

# Child Class: Chicken
class Chicken(Animal):
    def __init__(self, name, age, egg_count):
        super().__init__(name, age, "Cluck")
        self._egg_count = egg_count

    def lay_eggs(self):
        if self.health > 20:
            print(f"{self.name} lays {self._egg_count} eggs daily.")
            self.reduce_health(10)  # Reduce health by 10
        else:
            print(f"{self.name} is too weak to lay eggs!")

# Child Class: Dog
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, "Woof")
        self._breed = breed

    def guard(self):
        if self.health > 25:
            print(f"{self.name} the {self._breed} breed is guarding the farm!")
            self.reduce_health(20)  # Reduce health by 20
        else:
            print(f"{self.name} is too tired to guard!")

# Farm Class
class Farm:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def feed_all(self):
        for animal in self.animals:
            animal.eat("feed")

    def display_all(self):
        print("\n--- Farm Animals ---")
        for animal in self.animals:
            animal.display_info()

    def interact_with_animal(self, name):
        for animal in self.animals:
            if animal.name == name:
                if isinstance(animal, Cow):
                    animal.produce_milk()
                elif isinstance(animal, Chicken):
                    animal.lay_eggs()
                elif isinstance(animal, Dog):
                    animal.guard()
                return
        print("Animal not found!")

# Main Menu
def main_menu():
    my_farm = Farm()
    while True:
        print("\n--- Farm Management System ---")
        print("\n--- Choose one of them to continue ---")
        print("1. Add Animal")
        print("2. Feed All Animals")
        print("3. Display All Animals")
        print("4. Interact with Animal")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            animal_type = input("Enter animal type (Cow/Chicken/Dog): ").strip().lower()
            name = input("Enter animal name: ")
            age = int(input("Enter animal age: "))

            if animal_type == 'cow':
                milk_production = int(input("Enter milk production (liters per day): "))
                my_farm.add_animal(Cow(name, age, milk_production))
            elif animal_type == 'chicken':
                egg_count = int(input("Enter egg count per day: "))
                my_farm.add_animal(Chicken(name, age, egg_count))
            elif animal_type == 'dog':
                breed = input("Enter dog breed: ")
                my_farm.add_animal(Dog(name, age, breed))
            else:
                print("Invalid animal type!")

        elif choice == '2':
            my_farm.feed_all()

        elif choice == '3':
            my_farm.display_all()

        elif choice == '4':
            my_farm.display_all() 
            name = input("Enter animal name to interact: ")
            my_farm.interact_with_animal(name)

        elif choice == '5':
            print("Exiting the farm management system.")
            break

        else:
            print("Invalid choice! Please select a valid option.")
# Run the main menu
main_menu()()