class Car:

    def __init__(self, vehicle_num, driver_age, slot_id=None):
        self.vehicle_num = vehicle_num
        self.driver_age = driver_age
        self.slot_id = slot_id

    def assign_ticket(self, vehicle_num):
        self.vehicle_num = vehicle_num
