class Walking:
    def __init__(self, walk_speed, legs):
        self.walk_speed = walk_speed
        self.legs = legs

    def walk(self):
        print(f"Walks at {self.walk_speed} MPH using its {self.legs} legs.")