def generate_line(cell_width, num_columns, separator, char):
    return separator + ((char * cell_width + separator) * num_columns)


def empty_line(cell_width, num_columns):
    return generate_line(cell_width, num_columns, "|", " ")


def separator_line(cell_width, num_columns):
    return generate_line(cell_width, num_columns, "+", "-")


def print_simple_grid(cell_width, cell_height, data):
    for idx, row in enumerate(data):
        num_columns = len(row)
        if idx == 0:
            print(separator_line(cell_width, num_columns))
        line = "|"
        for cell_data in row:
            cell_padding = cell_width - len(cell_data)
            line += (cell_data[:cell_width] + " " * cell_padding) + "|"
        print(line)
        for _ in range(1, cell_height):
            print(empty_line(cell_width, num_columns))
        print(separator_line(cell_width, num_columns))


EXAMPLE_1 = 4, 2, [["abc", "def"], ["1234", "12"]]

EXAMPLE_2 = 4, 2, [["abcABC", "def"], ["1234", "12"]]


if __name__ == "__main__":
    cell_width, cell_height, data = EXAMPLE_2
    print_simple_grid(cell_width, cell_height, data)
    print()
    # cell_width, cell_height, data = EXAMPLE_2
    # print_simple_grid(cell_width, cell_height, data)
