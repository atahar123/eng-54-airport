# flught trip class

# origin
# destination
# list of passengers
# plane number

# need some getters and setters

# as a user I can add a plane
# as a user I can add a destination
# as a user I can add an origin

# as a user I can add a passenger names

class flight_trip:
    def __init__(self, origin, destination, plane_number, passengers=[]):
        self.origin = origin
        self.destination = destination
        self.plane_number = plane_number
        self.__passengers = passengers

    def get_passengers(self):
        return self.__passengers

    def set_passengers(self, entry):
        self.__passengers.append(entry)
        return "New passenger: " + entry
    