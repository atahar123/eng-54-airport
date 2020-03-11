# aircraft class

# attributes: cargo
# define a couple of methods, accelerate and break


class Aircraft():
    # define behaviours and characteristics
    def __init__(self, cargo, plane):
        self.cargo = cargo
        self.plane = plane

    # methods
    def accelerate(self):
        return 'Very quickly'

    def p_break(self):
        return 'In time'
