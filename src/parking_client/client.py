from src.car_parking_sys import CarParkingSystem

server = None


def initialize_server(srv, *args):
    global server
    if server is None:
       server = CarParkingSystem(args[0])
    else:
        raise Exception("Server is already initialized")


def park_a_car(srv, *args):
    if srv is not None:
        return srv.book(*args)


def lookup_slot_number_for_driver_of_age(srv, *args):
    if srv is not None:
        return None


def lookup_slot_number_for_car_with_number(srv, *args):
    if srv is not None:
        return srv.get_slot_for_vehicle_with_number(*args)


def leave_parking(srv, *args):
    if srv is not None:
        return srv.exit(*args)


def list_vehicle_registration_numbers_for_driver_of_age(srv, *args):
    if srv is not None:
        return None


class ClientCarParkingSystem:
    literal_action_map = {
        "Create_parking_lot": initialize_server,
        "Park": park_a_car,
        "Slot_numbers_for_driver_of_age": lookup_slot_number_for_driver_of_age,
        "Slot_number_for_car_with_number": lookup_slot_number_for_car_with_number,
        "Leave": leave_parking(),
        "Vehicle_registration_number_for_driver_of_age": list_vehicle_registration_numbers_for_driver_of_age(),
    }

    def run_commands(self, commands=list()):
        for cmd in commands:
            cmd_args = cmd.split(" ")
            action = cmd_args[0]
            args = cmd_args[1:]
            if action not in self.literal_action_map:
                raise Exception("Invalid command")
            return self.literal_action_map[action](server, args)
