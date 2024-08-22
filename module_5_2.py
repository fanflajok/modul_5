class House:
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

h1 = House("Luigi's Mansion", 16)
h2 = House("Princess Peach's Castle", 3)
h1.go_to(3)
h2.go_to(4)
print(len(h1))
print(len(h2))
print(h1.__str__())
print(h2.__str__())
