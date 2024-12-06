import random
from abc import ABC, abstractmethod

class EcosystemEntity(ABC):
    def __init__(self, name, energy, position, survival_rate):
        self.name = name
        self.energy = energy
        self.position = position
        self.survival_rate = survival_rate

    @abstractmethod
    def act(self, ecosystem):
        pass

    def move(self, map_size):
        dx, dy = random.choice([(0, 1), (1, 0), (0, -1), (-1, 0)])
        new_x = max(0, min(self.position[0] + dx, map_size[0] - 1))
        new_y = max(0, min(self.position[1] + dy, map_size[1] - 1))
        self.position = (new_x, new_y)
        self.energy -= 2

class Plant(EcosystemEntity):
    def __init__(self, position):
        super().__init__("Plant", 10, position, 1.0)

    def act(self, ecosystem):
        self.energy += 5
        if self.energy >= 20:
            self.energy -= 10
            ecosystem.add_entity(Plant(self.position))
            print(f"A new Plant was born at {self.position}.")

class Animal(EcosystemEntity):
    def __init__(self, name, energy, position, survival_rate, speed, food_types):
        super().__init__(name, energy, position, survival_rate)
        self.speed = speed
        self.food_types = food_types

    def eat(self, ecosystem):
        for entity in ecosystem.get_entities_in_area(self.position, 3):
            if type(entity) in self.food_types:
                self.energy += entity.energy
                ecosystem.remove_entity(entity)
                print(f"{self.name} ate {entity.name} at {entity.position}.")
                return True
        return False

    def reproduce(self, ecosystem):
        thresholds = {"Herbivore": 30, "Carnivore": 40, "Omnivore": 35}
        energy_loss = {"Herbivore": 15, "Carnivore": 20, "Omnivore": 18}
        if self.energy >= thresholds[self.name]:
            self.energy -= energy_loss[self.name]
            child_position = self.position
            child = type(self)(child_position)
            ecosystem.add_entity(child)
            print(f"A new {self.name} was born at {child_position}.")

    def act(self, ecosystem):
        self.move(ecosystem.map_size)
        if not self.eat(ecosystem):
            self.energy -= 1
        self.reproduce(ecosystem)
        if self.energy <= 0:
            print(f"{self.name} at {self.position} has died.")
            ecosystem.remove_entity(self)

class Herbivore(Animal):
    def __init__(self, position):
        super().__init__("Herbivore", 20, position, 0.8, 1, [Plant])

class Carnivore(Animal):
    def __init__(self, position):
        super().__init__("Carnivore", 25, position, 0.9, 2, [Herbivore, Omnivore])

class Omnivore(Animal):
    def __init__(self, position):
        super().__init__("Omnivore", 30, position, 0.85, 1, [Plant, Herbivore])

class Ecosystem:
    def __init__(self, map_size):
        self.map_size = map_size
        self.entities = []

    def add_entity(self, entity):
        self.entities.append(entity)

    def remove_entity(self, entity):
        self.entities.remove(entity)

    def get_entities_in_area(self, position, radius):
        x, y = position
        return [
            e for e in self.entities
            if abs(e.position[0] - x) <= radius and abs(e.position[1] - y) <= radius and e != position
        ]

    def step(self):
        for entity in self.entities[:]:
            entity.act(self)

    def display(self):
        grid = [["." for _ in range(self.map_size[1])] for _ in range(self.map_size[0])]
        for entity in self.entities:
            x, y = entity.position
            grid[x][y] = entity.name[0]
        print("\n".join("".join(row) for row in grid))

eco = Ecosystem(map_size=(30, 30))
for _ in range(10):
    eco.add_entity(Plant((random.randint(0, 29), random.randint(0, 29))))
for _ in range(3):
    eco.add_entity(Herbivore((random.randint(0, 29), random.randint(0, 29))))
for _ in range(1):
    eco.add_entity(Carnivore((random.randint(0, 29), random.randint(0, 29))))
for _ in range(2):
    eco.add_entity(Omnivore((random.randint(0, 29), random.randint(0, 29))))

steps = 10
for step in range(steps):
    print(f"\nStep {step + 1}")
    eco.step()
    eco.display()
