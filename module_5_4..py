class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)
    def __init__(self, appart_comp_name, number_of_floors):
        self.appart_comp_name = appart_comp_name
        self.number_of_floors = int(number_of_floors)
    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print(f"There's no floor № {new_floor} in {self.appart_comp_name}")
        else:
            for i in range(new_floor):
                print(i+1)
            print(f"You have arrived on the {i+1} floor in the {self.appart_comp_name}")
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return (f"There are {self.number_of_floors} floors in the {self.appart_comp_name}")
    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors
    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors
    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors
    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors
    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors
    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors
    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
            print(f"Numbers of floors in {self.appart_comp_name} was increased by {value}")
        return self
    def __radd__(self, value):
        return self.__add__(value)
    def __iadd__(self, value):
        return self.__add__(value)
    def __del__(self):
        print(f"{self.appart_comp_name} was demolished, but it will remain in history")
h1 = House("Luigi's Mansion", 16)
h2 = House("Princess Peach's Castle", 3)
h3 = House("Toad's Home", 2)
h4 = House("Twinsan's House", 3)
print(House.houses_history)
h1.go_to(1)
h2.go_to(1)
print(len(h1))
print(len(h2))
print(h1)
print(h2)
print(h1==h2)
h2 = h2 + 13
print(h1)
print(h1==h2)
h2 += 4
print(h2)
h1 = h1 + 4
h3 = h3 + 6
h4 = h4 + 10


print(h1 < h2)
print(h1 <= h2)
print(h1 > h2)
print(h1 >= h2)
print(h1 != h2)

del h1
del h2
del h3
del h4
print("Demolished buildings: ", House.houses_history)