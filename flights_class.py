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
    def __init__(self, origin, destination, plane_number):
        self.origin = origin
        self.destination = destination
        self.plane_number = plane_number
        self.__passengers_list = []

    def add_passengers(self, input_passenger):
        self.passengers_list.append([input_passenger])