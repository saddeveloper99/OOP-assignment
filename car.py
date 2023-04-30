class Car():
    def __init__(self, model, color):
        self.model = model
        self.color = color
        self.speed = 0

    def accelerate(self, speed):
        self.speed += speed
        self.speed = min(self.speed, 200)

    def brake(self, speed):
        self.speed -= speed
        self.speed = max(self.speed, 0)

    def get_speed(self):
        return self.speed


car1 = Car("Shopping Cart", "Red")
# car2 = Car("Rickshaw")

car1.accelerate(50)
print(car1.speed)

car1.brake(20)
print(car1.speed)

car1.brake(60)
print(car1.speed)
