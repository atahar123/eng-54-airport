# define plane class
# it inherits from aircraft

# attributes it needs:
    # plane_number

from aircraft_class import *

class Plane(Aircraft):

    def __init__(self, plane_number, cargo):
        super().__init__(cargo)
        self.plane_number = plane_number