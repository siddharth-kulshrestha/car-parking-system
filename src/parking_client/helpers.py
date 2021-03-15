from src.utils import extract_drivers_age, convert_args_to_int


@convert_args_to_int
@extract_drivers_age
def park_a_car(srv, *args):
    if srv is not None:
        return srv.book(*args)


@convert_args_to_int
def lookup_slot_number_for_driver_of_age(srv, *args):
    if srv is not None:
        return srv.lookup_slot_numbers_for_car_with_drivers_age(*args)


@convert_args_to_int
def lookup_slot_number_for_car_with_number(srv, *args):
    if srv is not None:
        return srv.lookup_slot_number_for_car_with_number(*args)


@convert_args_to_int
def leave_parking(srv, *args):
    if srv is not None:
        return srv.exit(*args)


@convert_args_to_int
def list_vehicle_registration_numbers_for_driver_of_age(srv, *args):
    if srv is not None:
        return srv.lookup_slot_numbers_for_car_with_drivers_age(*args)
