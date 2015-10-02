import random
import numpy as np

class Car():

    def __init__(self, max_kph = 120, current_speed = 0, length = 5,
                start_location = 0, in_front = None):
        self.max_kph = max_kph
        self.current_speed = current_speed
        self.length = length
        self.location = start_location
        self.in_front = in_front

    @property
    def move_forward(self):
        self.change_velocity()
        self.location += self.current_speed

    @property
    def translate_max(self):
        return self.max_kph / 3.6

    def accelerate(self):
        if self.current_speed < self.translate_max:
            self.current_speed += 2

    def can_decelerate(self):
        if random.random() <= .1:
            return True
        return False

    def decelerate(self):
        if self.current_speed > 0:
            self.current_speed -= 2

    def change_velocity(self):
        if self.can_decelerate():
            self.decelerate()
        else:
            self.accelerate()

    def keep_distance(self):
        if self.in_front.location <= self.location + self.current_speed + 6:
            self.current_speed = self.in_front.current_speed

class Road():

    def __init__(self, road_length = 1000):
        self.road_length = road_length

class Simulation:

    def __init__(self, num_cars = 30, length = 1000):
        self.num_cars = num_cars
        self.length = length
        self.cars = self.create_cars()

    def create_cars(self):
        cars = []
        locations = np.linspace(0, self.length - 33, self.num_cars)
        for num in range(self.num_cars):
            if num == 0:
                old_car = None
            new_car = Car(start_location = locations[num],
                          in_front = old_car)
            cars.append(new_car)
            old_car = new_car
        return cars

    def run_simulation(self):
        for _ in range(60):
            self.simulate()

    def simulate(self):
        for car in self.cars:
            new_car.move_forward()

    def report(self):
        return [car.location for car in self.cars]
