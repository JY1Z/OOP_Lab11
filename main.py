#1
class Publication:
    def __init__(self,name):
        self.name = name

class Book(Publication):
    def __init__(self,name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count
    def print_information(self):
        print(f"{self.name} (author {self.author}, {self.page_count}pages)")


class Magazine(Publication):
    def __init__(self,name,  chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor
    def print_information(self):
        print(f"{self.name} (chief editor {self.chief_editor}")

book = Book("Compartment No. 6","Rosa Liksom",192)
magazine = Magazine("Donald Duck","Aki Hyyppä)")
book.print_information()
magazine.print_information()
#wrong: print_information(book)

#2
class Car:
    def __init__(self,registration_number,max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0
    def accerelate(self,change_of_speed):
        self.current_speed += change_of_speed
        if self.current_speed >= self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed <= 0:
            self.current_speed = 0
    def drive(self,hours):
        self.travelled_distance = self.travelled_distance + self.current_speed * hours
        return self.travelled_distance

class ElectricCar(Car):
    def __init__(self, registration_number,max_speed,battery_capacity):
        super().__init__(registration_number,max_speed)
#    def __init__(self,battery_capacity):
#        super().__init__()
        self.battery_capacity = battery_capacity

class GasolineCar(Car):
    def __init__(self, registration_number,max_speed,tank_volume):
        super().__init__(registration_number,max_speed)
        self.tank_volume = tank_volume

ecar = ElectricCar("ABC-15",180,52.5)
gcar = GasolineCar("ACD-123",165,32.3)
ecar.current_speed = 120
gcar.current_speed = 95
print(f"Electric Car:{ecar.drive(3)}")
print(f"Gasoline Car:{gcar.drive(3)}")
