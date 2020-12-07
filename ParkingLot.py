from Car import Car


class ParkingLot:
    instance = None

    @staticmethod
    def getInstance():
        if ParkingLot.instance is None:
            ParkingLot()
        return ParkingLot.instance

    def __init__(self, capacity):
        self.capacity = capacity
        self.num_of_occupied_slots = 0
        self.slot_id = 0
        self.slots = [0] * int(capacity)
        if ParkingLot.instance is not None:
            raise Exception("This class is a singleton!")
        else:
            ParkingLot.instance = self

    def get_immediate_empty_slot(self):
        return next((elem for elem in range(len(self.slots)) if self.slots[elem] == 0), 0)

    def assign_vehicle_parking(self, vehicle_no, age):
        # print("Immediate Slot ID %s" % self.get_immediate_empty_slot())
        if self.num_of_occupied_slots < self.capacity:
            slot_id = self.get_immediate_empty_slot()+1
            self.slots[slot_id] = Car(vehicle_no, age, slot_id)
            self.slot_id += 1
            self.num_of_occupied_slots += 1
            print("Car with vehicle registration number \"%s\" has been parked at slot number %s"
                  % (vehicle_no, self.slot_id))
            return self.slot_id
        else:
            return -1

    def leave_the_parking_lot(self, slot_id):
        if self.num_of_occupied_slots > 0 and self.slots[slot_id - 1] != 0:
            vehicle_num, driver_age= self.slots[slot_id-1].vehicle_num, self.slots[slot_id-1].driver_age
            print("Slot number %s vacated, the car woth vehicle registration number %s left the space, the driver of "
                  "the car was if the age %s" % (slot_id, vehicle_num, driver_age))
            self.slots[slot_id - 1] = 0
            self.num_of_occupied_slots = self.num_of_occupied_slots - 1
            return True
        else:
            return False

    def slot_numbers_for_driver_of_age(self, age):
        new_slot = []
        for i in range(len(self.slots)):
            if isinstance(self.slots[i], Car):
                if int(self.slots[i].driver_age) == age:
                    new_slot.append(self.slots[i].slot_id)
        return new_slot

    def slot_number_for_car_with_number(self, vehicle_num):
        print("Hekllo %s" % vehicle_num)
        for i in range(len(self.slots)):
            if isinstance(self.slots[i], Car):
                print(self.slots[i].__dict__)
                if int(self.slots[i].vehicle_num) == vehicle_num:
                    return self.slots[i].slot_id

