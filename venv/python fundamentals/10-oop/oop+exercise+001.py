class Vehicle:
    def __init__(self, name, price, type = "none", color = "none"):
        self.name = name
        self.type = "automobile"
        self.color = "black"
        self.price = price
    def description(self):
        print(f"The name of the vehicle is: {self.name}, its a {self.type}, colored {self.color}, worth {self.price} EUR")

    v_list = []

    range(3)
    for i in range(3):
        name = input("Please input vehicle name:")
        price = input("Please input type of the vehicle:")
        if input("would you like to provide type and color?") == "yes":
            type = input("Please input vehicle type:")
            color = input("Please input color of the vehicle:")
            vehicle1 = Vehicle(name, price, type, color)
            v_list.append(vehicle1)
        else:
            vehicle1 = Vehicle(name, price)
            v_list.append(vehicle1)

    for v in v_list:
        v.description()

vehicle1 = Vehicle("BMW",10000)
vehicle1.description()