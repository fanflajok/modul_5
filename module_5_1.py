class House:
    def __init__(self, appart_comp_name, number_of_floors):
        self.appart_comp_name = appart_comp_name
        self.number_of_floors = int(number_of_floors)
    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print(f"There's no floor № {new_floor} in {self.appart_comp_name}")
        else:
            for i in range(1, new_floor):
                print(i)
            print(f"You have arrived on the {i+1} floor in the {self.appart_comp_name}")

h1 = House("Luigi's Mansion", 16)
h2 = House("Princess Peach's Castle", 3)
h1.go_to(15)
h2.go_to(4)