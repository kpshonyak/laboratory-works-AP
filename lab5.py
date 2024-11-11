from enum import Enum

class Kind(Enum):
    DOG = "Dog"
    CAT = "Cat"
    BIRD = "Bird"
    FISH = "Fish"

class Pet:
    def __init__(self, name=None, breed=None, gender=None, age=None, greeting=None, mass=None, kind=None):
        self.name = name
        self.breed = breed
        self.gender = gender
        self.age = age
        self.greeting = greeting
        self.mass = mass
        self.kind = kind

    def __del__(self):
        print(f"Улюбленець {self.name} видалений")

    def __str__(self):
        return f"\n{self.name} ({self.kind.value}) - {self.age} y.o, Порода: {self.breed} \n Маса: {self.mass}кг, Стать: {self.gender}"

    def isPolite(self):
        return "Hello" in self.greeting


class Home:
    def __init__(self):
        self.pets = []

    def add_pet(self, pet):
        self.pets.append(pet)

    def display_pets(self):
        for pet in self.pets:
            print(pet)

    def sort_by_age(self):
        print("За зростанням:"),self.pets.sort(key=lambda pet: pet.age)
        self.display_pets()
        print("За спаданням:"),self.pets.sort(key=lambda pet: pet.age,reverse=True)
        self.display_pets()

    @staticmethod
    def areFriends(pets):
        friends = []
        for i in range(len(pets)):
            for j in range(i + 1, len(pets)):
                if abs(pets[i].age - pets[j].age) < 2:
                    friends.append((pets[i], pets[j]))
        return friends
    
    def partner_for_pet(self, chosen_pet, found_partners):
        partners = []
        for home in all_homes:
            if home != self:
                for pet in home.pets:
                    if (pet.kind == chosen_pet.kind and
                        pet.breed == chosen_pet.breed and
                        pet.gender != chosen_pet.gender and 
                        abs(pet.age - chosen_pet.age) <= 5):
                        if (chosen_pet.name, pet.name) not in found_partners and (pet.name, chosen_pet.name) not in found_partners:
                            partners.append((chosen_pet, pet))
                            found_partners.add((chosen_pet.name, pet.name))
        return partners


def main():
    
    pets1 = [
        Pet("Чіназес", "Пітбуль", "Male", 3, "Hello", 30, Kind.DOG),
        Pet("Кузя", "Британець", "Female", 4, "Hi there", 5, Kind.CAT),
        Pet("Красунчик", "канарейка", "Male", 1, "Hello", 0.2, Kind.BIRD),
        Pet("Пес", "Німецька вівчарка", "Female", 2, "Woof", 25, Kind.DOG)
    ]

    pets2 = [
        Pet("Барсик", "Пітбуль", "Female", 4, "Hello", 32, Kind.DOG),
        Pet("Грета", "Британська кішка", "Male", 2, "Meow", 6, Kind.CAT),
        Pet("Ласка", "канарейка", "Female", 3, "Hello", 0.3, Kind.BIRD),
        Pet("Рекс", "Німецька вівчарка", "Male", 5, "Woof", 28, Kind.DOG)
    ]
    pets3 = [
        Pet("Барсик", "Пітбуль", "Female", 4, "Hello", 32, Kind.DOG),
        Pet("Грета", "Британська кішка", "Male", 2, "Meow", 6, Kind.CAT),
        Pet("Ласка", "канарейка", "Female", 3, "Hello", 0.3, Kind.BIRD),
        Pet("Рекс", "Німецька вівчарка", "Male", 5, "Woof", 28, Kind.DOG)
    ]
    my_home1 = Home()
    my_home2 = Home()
    my_home3 = Home()

    for pet in pets1:
        my_home1.add_pet(pet)
    for pet in pets2:
        my_home2.add_pet(pet)
    for pet in pets3:
        my_home3.add_pet(pet)


    global all_homes
    all_homes = [my_home1, my_home2,my_home3]

    found_partners = set()

    for index, home in enumerate(all_homes, start=1):
        print(f"\nДомівка {index}:\n Список домашніх улюбленців:")
        home.display_pets()

        print("\nПеревірка ввічливості:")
        for pet in home.pets:
            print(f"{pet.name} ввічливий?", pet.isPolite())

        print("\nДрузі серед улюбленців:")
        friends = Home.areFriends(home.pets)
        for pet1, pet2 in friends:
            print(f"{pet1.name} і {pet2.name} є друзями!")

        print("\nСписок улюбленців, відсортований за віком:")
        home.sort_by_age()
    
    print("\nПошук партнера для улюбленців:")
    for home in all_homes:
        for pet in home.pets:
            partners = home.partner_for_pet(pet, found_partners)
            if partners:
                for chosen_pet, partner in partners:
                    print(f"\nЗнайдено партнера для {chosen_pet.name}: {partner.name}")
            else:
                print(f"\nДля {pet.name} партнера не знайдено.")

main()

