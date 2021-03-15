
def extract_drivers_age(server_operation):
    def wrapper_server_operation(srv, *args):
        args_modified = list(args)
        args_modified.remove("driver_age")
        return server_operation(srv, *args_modified)
    return wrapper_server_operation


def convert_args_to_int(server_operation):
    def wrapper_server_operation(srv, *args):
        modified_args = list()
        for arg in args:
            if arg.strip().isdigit():
                modified_args.append(int(arg))
                continue
            modified_args.append(arg)
        return server_operation(srv, *modified_args)
    return wrapper_server_operation
