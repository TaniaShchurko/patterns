import datetime
from random import randrange
from copy import deepcopy

class Photo:

    def __init__(self, name: str, date=datetime.datetime.now(), size=randrange(7,10), editing=False, program="camera"):
        self.name = name
        self.date = date
        self.size = size
        self.editing = editing
        self.program = program

    def __repr__(self):
        output = f"{self.name} was taken on {self.date}, size {self.size}MB. Wasn`t editing ({self.program})."
        updating = f"{self.name} was edited on {self.date}, new size {self.size}MB. Was editing by {self.program}"
        return output if self.editing is False else updating

    def update(self, program, size=randrange(2, 7),  editing=True):
        self.date = datetime.datetime.now()
        self.program = program
        self.size = size
        self.editing = editing

    @classmethod
    def enter(cls):
        name = str(input("Enter name of your photo: "))
        return Photo(name)

    def create_snapshot(self):
        return Snapshot(self)

class Snapshot:

    def __init__(self, temp):
        self.temp = deepcopy(temp)

    def restore(self):
        return self.temp

class backUp:
    def __init__(self, backup = None):
        self.backup = deepcopy(backup)

    @staticmethod
    def make_backup(obj):
        print("Backup was created.")
        return backUp(Photo.create_snapshot(obj))

    def undo(self):
        if self.backup is not None:
            return Snapshot.restore(self.backup)


photo = Photo.enter()
print(photo)
bk = backUp().make_backup(photo)
check = str(input("Do you want to update your photo? "))
if check.lower() == "yes":
    programs = str(input("Which program do you want to use? "))
    photo.update(programs)
    print(photo)
    print("Returning to previous version.")
    photo_new = bk.undo()
    print(photo_new)
elif check.lower() == "no":
    print("Okay.")
else:
    print("You enter incorrect answer")
