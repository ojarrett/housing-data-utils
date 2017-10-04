CSV_HEADER_LINES = [0, 1]
CSV_DELIMITER = ","

def merge_header_lines(header_lines):
    short_line = header_lines[0]
    long_line = header_lines[1]

    if len(header_lines[0]) > len(header_lines[1]):
        short_line = header_lines[1]
        long_line = header_lines[0]

    return [short_line[i] + " " + long_line[i] for i in range(len(short_line))] + [long_line[i] for i in range(len(short_line), len(long_line))]
