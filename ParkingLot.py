class ParkingLot:
    instance = None

    @staticmethod
    def getInstance():
        if ParkingLot.instance is None:
            ParkingLot()
        return ParkingLot.instance

    def __init__(self):
        if ParkingLot.instance is not None:
            raise Exception("This class is a singleton!")
        else:
            ParkingLot.instance = self
