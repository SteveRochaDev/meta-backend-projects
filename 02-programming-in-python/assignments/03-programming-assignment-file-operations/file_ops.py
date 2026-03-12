def read_file(file_name):
    """ Reads and returns the entire contents of a file as a single string."""
    with open(file_name, 'r') as file:
        contents = file.read()
    print(contents)
    return contents


def read_file_into_list(file_name):
    """ Reads a file line-by-line and returns a list where each element is a line."""
    lines = []
    with open(file_name, 'r') as file:
        for line in file:
            lines.append(line)  # keep the newline characters!
    return lines


def write_first_line_to_file(file_contents, output_filename):
    """ Writes the first line of file_contents to output_filename."""
    first_line = file_contents.split('\n')[0]  # everything before first newline
    with open(output_filename, 'w') as file:
        file.write(first_line)


def read_even_numbered_lines(file_name):
    """ Returns a list of even-numbered lines (2, 4, 6, ...) from the file."""
    even_lines = []
    with open(file_name, 'r') as file:
        for idx, line in enumerate(file, start=1):
            if idx % 2 == 0:
                even_lines.append(line)  # keep newline
    return even_lines


def read_file_in_reverse(file_name):
    """ Reads the file and returns a list of its lines in reverse order."""
    with open(file_name, 'r') as file:
        lines = file.readlines()  # keeps newlines
    reversed_lines = lines[::-1]
    print(reversed_lines)
    return reversed_lines


# Sample commands to test the functions
def main():
    file_contents = read_file("sampletext.txt")
    print("File Contents:\n", file_contents)

    print("\nFile as List:", read_file_into_list("sampletext.txt"))

    write_first_line_to_file(file_contents, "output.txt")
    print("\nFirst line written to output.txt")

    print("\nEven-numbered lines:", read_even_numbered_lines("sampletext.txt"))

    print("\nFile in Reverse Order:")
    read_file_in_reverse("sampletext.txt")


if __name__ == "__main__":
    main()