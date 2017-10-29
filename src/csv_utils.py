CSV_HEADER_LINES = [0, 1]
CSV_DELIMITER = ","

def get_header_lines_from_file(file_path, translate=True):
    header = None

    with open(file_path, "r") as input_file:
        header_lines = [input_file.readline().strip().split(CSV_DELIMITER) for line in CSV_HEADER_LINES]

        # Columns in housing CSV files show up as ",,1-unit,," instead of "1-unit,1-unit,1-unit"
        if translate:
            for i in range(len(header_lines[0])):
                if header_lines[0][i] == "" and i < len(header_lines[0]) - 1 and "unit" in header_lines[0][i+1]:
                    header_lines[0][i] = header_lines[0][i+1]
                if header_lines[0][i] == "" and "units" in header_lines[0][i-1]:
                    header_lines[0][i] = header_lines[0][i-1]

            header_lines[0].append(header_lines[0][len(header_lines[0])-1])


        header = merge_header_lines(header_lines)

    if header is None:
        print("Failed to extract header lines. Exiting...")
        exit(1)

    return header

def merge_header_lines(header_lines):
    short_line = header_lines[0]
    long_line = header_lines[1]

    if len(header_lines[0]) > len(header_lines[1]):
        short_line = header_lines[1]
        long_line = header_lines[0]

    return [short_line[i] + " " + long_line[i] for i in range(len(short_line))] + [long_line[i] for i in range(len(short_line), len(long_line))]
