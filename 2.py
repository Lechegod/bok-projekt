"""
class TemperatureSensor:
    def __init__(self, location, temperature):
        self.location = location
        self.temperature = temperature

    def increase_temperature(self):
        self.temperature += 1

    def decrease_temperature(self):
        self.temperature -= 1

    def show_temperature(self):
         print(f"{self.location}: {self.temperature} degrees")

sensor1 = TemperatureSensor("Kitchen", 20)
sensor2 = TemperatureSensor("Bedroom", 18)

sensor1.show_temperature()
sensor2.show_temperature()

sensor1.increase_temperature()
sensor1.increase_temperature()

sensor2.decrease_temperature()

sensor1.show_temperature()
sensor2.show_temperature()
"""
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def sell(self):
        if self.stock <= 0:
            print("Produkten är slut i lager:(")
        else:
            self.stock -= 1

    def show_info(self):
        print(f"Produkt: {self.name}")
        print(f"Pris: {self.price} kr")
        print(f"Lager: {self.stock}")

    def restock(self, amount):
        self.stock += amount


product1 = Product("Tangentbord", 399, 10)

product1.sell()
product1.show_info()

product1.restock(5)
product1.show_info()