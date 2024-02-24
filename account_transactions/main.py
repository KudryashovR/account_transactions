import utils


def main():
    filename = "operations.json"

    operations_json = utils.load_operations(filename)
    operations_list = utils.init_operations(operations_json)


if __name__ == "__main__":
    main()
