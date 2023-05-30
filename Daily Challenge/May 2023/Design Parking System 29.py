# # Challenge Context
# Design a parking system for a parking lot. The parking lot has three kinds of parking spaces: big, medium, and small, with a fixed number of slots for each size.

# Challenge Link --> https://leetcode.com/problems/design-parking-system/


class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.big_slots = big
        self.medium_slots = medium
        self.small_slots = small

    def addCar(self, carType: int) -> bool:
        if carType == 1 and self.big_slots >= 1:
            self.big_slots -= 1
        elif carType == 2 and self.medium_slots >= 1:
            self.medium_slots -= 1
        elif carType == 3 and self.small_slots >= 1:
            self.small_slots -= 1
        else:
            return False
        return True


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
