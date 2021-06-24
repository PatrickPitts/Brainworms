# Author : John Patrick Pitts
# Date   : June 24, 2021
# File   : Lab 7, People.py

# Parent class
class Human:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def hobby(self):
        print("Likes dank memes")

    def info(self):
        print("Name: ", self.name)
        print("Age: ", self.age)


# inherits from Human
class Hiker(Human):
    def hobby(self):
        print("Likes to go hiking")


# inherits from Human
class Scientist(Human):
    def __init__(self, age, name, lab):
        Human.__init__(self, age, name)
        self.lab = lab

    def hobby(self):
        print("Likes studying scientific fields")

    def labName(self):
        print("Works at the {} lab.".format(self.lab))


# inherits from Human
class Swimmer(Human):
    def __init__(self, age, name, hours):
        Human.__init__(self, age, name)
        self.hours = hours

    def hobby(self):
        print("Likes to swim in lakes")

    def hoursSwimming(self):
        print("Swims {} hours a week".format(self.hours))


# inherits from Scientist and Swimmer
class ScientificSwimmer(Scientist, Swimmer):
    def __init__(self, age, name, lab, hours):
        Scientist.__init__(self, age, name, lab)
        Swimmer.__init__(self, age, name, hours)


def main():
    # initializes class instances of parent and child classes
    human = Human(25, "Alice")
    hiker = Hiker(30, "Bob")
    scientist = Scientist(37, "Cindy", "CERN")
    swimmer = Swimmer(22, "Douglas", 10)
    sciswim = ScientificSwimmer(34, "Eric", "LIGO", 15)

    # calls all functions on the various class instances
    human.info()
    human.hobby()
    print()

    hiker.info()
    hiker.hobby()
    print()

    scientist.info()
    scientist.hobby()
    scientist.labName()
    print()

    swimmer.info()
    swimmer.hobby()
    swimmer.hoursSwimming()
    print()

    sciswim.info()
    sciswim.hobby()
    sciswim.labName()
    sciswim.hoursSwimming()


if __name__ == "__main__":
    main()
