# SOLVED
class ParkingSystem(object):

    def __init__(self, big, medium, small):
        self.park = {1: big, 2: medium, 3:small}

    def addCar(self, carType):

        if self.park[carType] == 0:
            return False

        self.park[carType] -= 1
        return True


