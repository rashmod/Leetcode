# Design Simulation Counting

# Optimal
# time complexity: O(1)
# space complexity: O(1)
class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.size = {1: big, 2: medium, 3: small}
        self.avail = {1: big, 2: medium, 3: small}

    def addCar(self, carType: int) -> bool:
        if self.avail[carType] > 0:
            self.avail[carType] -= 1
            return True
        return False
