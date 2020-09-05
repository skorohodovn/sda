with open('example.txt') as f:
    for line_no, line in enumerate(f):
        print(f"{line_no}: {line.strip()}")
        if line_no == 1:
            continue

        clean_line = line.strip()
        print(f"Line £{line_no} --> {clean_line}")

