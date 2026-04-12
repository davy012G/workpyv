#File Name: test_script.py

import games.turtleGames as t
import toolKit.customTools as c
import games.eyeTest as e

root = t.tk.Tk()
t.Start(root)
root.mainloop()

# Program for testing both c and e
baseNumber = 15
class_name = e.BoardSet()
template = (20, baseNumber, 5)

for t in (class_name.heptagon, class_name.pentagon, class_name.octagon):
    c.AsciiCoordinates().drawOnBoard(baseNumber, t(*template))

"""
class Animal:

    sound = ""
    behaviour = ""

    def __init__(self) -> None:
        self.name = ""

    def _print(self):
        print(self.sound, ",", self.behaviour)

    def change_sound(self, audio):
        self.sound = audio
    
    def change_behaviour(self, trait):
        self.behaviour = trait

class Cat(Animal):

    def __init__(self):
        self.name = "Meowzer"
        self.change_sound("meow")
        self.change_behaviour("walk")

class Dog(Animal):

    def __init__(self) -> None:
        #super().__init__()
        self.name = "Poodle"
        self.change_sound("bark")
        self.change_behaviour("stroll")

meowzer = Cat()
poodle = Dog()
harry = Dog()
harry.behaviour = "dog-walk"

meowzer._print()
poodle._print()

print(poodle.behaviour)
print(harry.behaviour)
print(meowzer.behaviour)

\"""The idea behind this is that we want to see if they are the same thing or not if they are because of the 
lack of using name-specific variables then the theory is proved that the Animal class will need super().__init()
if it's gonna pass it's info to the other children in a way that will make them unique and not the same being.\"""

"""