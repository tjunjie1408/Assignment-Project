# utils.py

def read_file(filename):
    """Reads all lines from a file and returns as a list of lists (CSV-style)."""
    try:
        with open(filename, 'r') as file:
            return [line.strip().split(',') for line in file.readlines()]
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return []
    except IOError:
        print(f"Error reading file {filename}.")
        return []

def write_file(filename, data):
    """Writes a list of lists to a file in CSV-style format."""
    try:
        with open(filename, 'w') as file:
            for item in data:
                file.write(','.join(item) + "\n")
    except IOError:
        print(f"Error writing to file {filename}.")

def append_file(filename, entry):
    """Appends a single CSV-style entry to a file."""
    try:
        with open(filename, 'a') as file:
            file.write(','.join(entry) + "\n")
    except IOError:
        print(f"Error appending to file {filename}.")
