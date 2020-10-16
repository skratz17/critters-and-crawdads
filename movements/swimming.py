class Swimming:
    def __init__(self, swim_speed, maximum_depth):
        self.swim_speed = swim_speed
        self.maximum_depth = maximum_depth

    def swim(self):
        print(f"Swims at {self.swim_speed} MPH all the way down to {self.maximum_depth} feet below sea level or whatever.")