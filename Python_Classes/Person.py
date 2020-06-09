class Person():
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    # changes person's name to new_name
    def change_name(self, new_name):
        self.name = new_name

    # A birthday occured so increase the person's age by 1
    def birthday(self):
        self.age += 1

    # Random formula where every hour a person exercises, they lose 2 pounds.
    # Parameter time is in hours.
    def exercise(self, time):
        self.weight -= time * 2

    # String representation of the class
    def __str__(self):
        return 'Name: ' + self.name + '\n' + 'Age: ' + str(self.age) + ' \n' + 'Height: ' + str(self.height) + '\n' + 'Weight: ' + str(self.weight)

def main():
    person = Person('Bob', 23, 72, 180)

    print("Orignal attributes of person:")
    print(person)
    print()
    print("Change Name to Larry:")
    print("Old Name: " + person.name)
    person.change_name("Larry")
    print("New Name: " + person.name)
    print()
    print("Today is the Birthday:")
    print("Old Age: " + str(person.age))
    person.birthday()
    print("New Age: " + str(person.age))
    print()
    print("exercise for 2 hours")
    print("Old Weight: " + str(person.weight))
    person.exercise(2)
    print("New Weight: " + str(person.weight))
    print()
    print("New attributes of person")
    print(person)
    print()

main()
