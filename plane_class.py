# define plane class
# it inherits from aircraft

# attributes it needs:
    # plane_number

from aircraft_class import *

class Plane(Aircraft):

    def __init__(self, plane_number, cargo, plane):
        super().__init__(cargo, plane)
        self.plane_number = plane_number
        self.plane = plane
