class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.bigCar = big
        self.mediumCar =  medium
        self.smallCar = small

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.bigCar > 0:
                self.bigCar -= 1
                return True
        elif carType == 2:
            if self.mediumCar > 0:
                self.mediumCar -=1
                return True
        else:
            if self.smallCar > 0:
                self.smallCar -=1
                return True
        return False

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)