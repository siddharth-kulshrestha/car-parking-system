from src.car_parking_sys import CarParkingSystem
from .helpers import park_a_car, lookup_slot_number_for_car_with_number,\
    lookup_slot_number_for_driver_of_age, leave_parking, list_vehicle_registration_numbers_for_driver_of_age
from ..utils import convert_args_to_int

server = None


@convert_args_to_int
def initialize_server(srv, *args):
    global server
    if server is None:
        server = CarParkingSystem(args[0])
        return [args[0]]
    else:
        raise Exception("Server is already initialized")


class ClientCarParkingSystem:
    literal_action_map = {
        "Create_parking_lot": initialize_server,
        "Park": park_a_car,
        "Slot_numbers_for_driver_of_age": lookup_slot_number_for_driver_of_age,
        "Slot_number_for_car_with_number": lookup_slot_number_for_car_with_number,
        "Leave": leave_parking,
        "Vehicle_registration_number_for_driver_of_age": list_vehicle_registration_numbers_for_driver_of_age,
    }

    action_output_formatter_map = {
        "Create_parking_lot": "Created parking of {} slots",
        "Park": 'Car with vehicle registration number "{}" has been parked at slot number {}',
        "Leave": 'Slot number {} vacated, the car with vehicle registration number "{}" left the space, '
                 'the driver of the car was of age {}',
    }

    def run_commands(self, commands=None):
        if not commands:
            raise Exception("Need commands to execute")
        for cmd in commands:
            cmd = cmd.replace('\n', '')
            # print(cmd)
            cmd_args = cmd.split(" ")
            action = cmd_args[0]
            args = cmd_args[1:]
            if action not in self.literal_action_map:
                raise Exception("Invalid command")
            result = self.literal_action_map[action](server, *args)
            if action in self.action_output_formatter_map:
                result = self.action_output_formatter_map.get(action).format(*result)
            if isinstance(result, list):
                result = map(lambda x: str(x), result)
                result = ', '.join(result)
            print("{}".format(result))
