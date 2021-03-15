from .parking_slots import ParkingSlot

# TODO: Follow singleton pattern to allow one object to stay at runtime


class CarParkingSystem:

    def __init__(self, total_number_of_slots):
        self.total_number_of_slots = total_number_of_slots
        self.slot_dict = dict()
        self.vehicle_slot_mapping = dict()
        for slot in range(total_number_of_slots):
            self.slot_dict[slot] = ParkingSlot(slot)

    def book(self, vehicle_number, driver_age):
        # Finding first empty slot
        for slot_idx in range(self.total_number_of_slots):
            pslot = self.slot_dict.get(slot_idx)
            if pslot.is_available:
                self.vehicle_slot_mapping[vehicle_number] = pslot
                return pslot.book(vehicle_number, driver_age)

    def exit(self, pslot_id):
        if pslot_id not in self.slot_dict:
            raise Exception("Enter parking slot with correct range")
        if self.slot_dict.get(pslot_id).is_available:
            raise Exception("Parking slot with id is already available".format(pslot_id))
        pslot = self.slot_dict.get(pslot_id)
        vehicle_number = pslot.vehicle_number
        driver_age = pslot.driver_age
        pslot.mark_as_available()
        self.vehicle_slot_mapping.pop(vehicle_number)
        return pslot_id, vehicle_number, driver_age

    def lookup_slot_number_for_car_with_number(self, vehicle_number):
        if vehicle_number in self.vehicle_slot_mapping.keys():
            pslot = self.vehicle_slot_mapping.get(vehicle_number)
            return str(pslot.slot_id)
        return None

    def lookup_slot_numbers_for_car_with_drivers_age(self, age):
        req_slots = list()
        for slot_idx, pslot in self.slot_dict.items():
            if pslot and pslot.driver_age == age:
                req_slots.append(slot_idx)
        return req_slots







