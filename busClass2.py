# setting up the student class
class Bus:
    def __init__(self, route, bus_number, driver):
        self.route = route
        self.bus_number = bus_number
        self.driver = driver
        bus_list.append(self)


# Main routine
bus_list = []

bus1 = Bus("2010", "Y", "Greg")
bus2 = Bus("2011", "P", "Bob")
bus3 = Bus("2012", "130", "Baker")

for bus in bus_list:
    print(f"Bus number: {bus.bus_number} "
          f"on route {bus.route} "
          f"with driver: {bus.driver} ")




