import utils


def main():
    filename = "operations.json"

    operations_json = utils.load_operations(filename)
    operations_list = utils.init_operations(operations_json)
    operations_list.sort()
    utils.print_operations(operations_list)


if __name__ == "__main__":
    main()
