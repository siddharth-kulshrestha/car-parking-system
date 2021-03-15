
class ParkingSlot:

    def __init__(self, slot_id):
        self.slot_id = slot_id
        self.is_available = True
        self.vehicle_number = None
        self.driver_age = None

    def book(self, vehicle_number, driver_age):
        self.driver_age = driver_age
        self.vehicle_number = vehicle_number
        self.is_available = False
        return self.vehicle_number, self.slot_id

    def mark_as_available(self):
        self.is_available = True
        self.vehicle_number = None
        self.driver_age = None

    def __str__(self):
        return "{}::{}::{}::{}".format(self.slot_id, self.vehicle_number, self.driver_age, self.is_available)
