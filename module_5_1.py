class House:

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor <= 0 or new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            nf = 1
            while nf <= new_floor:
                print(nf)
                nf = nf + 1


h1 = House('ЖК Эльбрус', 30)
h2 = House('Просто дом', 2)
h1.go_to(5)
h2.go_to(5)
