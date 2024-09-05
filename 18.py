class House():

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor):
        if new_floor <= 0:
            return print("Такого этажа нет")
        if new_floor <= self.number_of_floors:
            for i in range(new_floor):
                if i < self.number_of_floors:
                    print(i+1)
        else:
            print("Такого этажа не существует")
    def __len__(self):
        return  (self.number_of_floors)
    def __str__(self):
        return f"Название: {self.name}, Количество этажей {self.number_of_floors})"
    def __eq__(self, other):
        if self.number_of_floors == other.number_of_floors:
            return True
        return False
    def __lt__(self, other):
        if self.number_of_floors < other.number_of_floors:
            return True
        return False
    def __le__(self, other):
        if self.number_of_floors <= other.number_of_floors:
            return True
        return False
    def __gt__(self, other):
        if self.number_of_floors > other.number_of_floors:
            return True
        return False
    def __ge__(self, other):
        if self.number_of_floors >= other.number_of_floors:
            return True
        return False
    def __ne__(self, other):
        if self.number_of_floors != other.number_of_floors:
            return True
        return False
    def __add__(self, value):
        self.number_of_floors+=value;
        return self
    def __radd__(self, value):
        self.number_of_floors+=value;
        return self.number_of_floors

a = House("Жк", 23)
b = House("Жк2", 23)
a.go_to(23)
print("\n")
print(a == b)
print(a >= b)
print(a != b)
print(a <= b)
print(a + 3)
print(3 + a)





