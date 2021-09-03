def skip_lines(input_file, skip):
    for i in range(0, skip):
        next(input_file)
