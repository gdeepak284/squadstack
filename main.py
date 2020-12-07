from ParkingLot import ParkingLot

if __name__ == '__main__':
    file = open('input.txt', 'r')
    lines = file.readlines()
    parkinglot = None
    for line in lines:
        a = line.rstrip().split(' ')
        if a[0] == 'Create_parking_lot':
            parkinglot = ParkingLot(int(a[1]))
            print("Created parking of %s slots" % parkinglot.capacity)
        elif a[0] == 'Park':
            vehicle_no = a[1]
            age = a[3]
            if int(age) >= 18:
                print("Assigned %s" % parkinglot.assign_vehicle_parking(vehicle_no, age))
            else:
                print("Driver is minor")
        elif a[0] == 'Slot_numbers_for_driver_of_age':
            print("The slot numbers of all cars which have drivers of age {0} are "
                  "{1}".format(a[1], parkinglot.slot_numbers_for_driver_of_age(int(a[1]))))
        elif a[0] == 'Leave':
            parkinglot.leave_the_parking_lot(int(a[1]))
        elif a[0] == 'Slot_number_for_car_with_number':
            print(parkinglot.slot_number_for_car_with_number(a[1]))
        elif a[0] == 'Vehicle_registration_number_for_driver_of_age':
            print("Vehicle_registration_number_for_driver_of_age")
