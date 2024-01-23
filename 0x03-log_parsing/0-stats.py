#!/usr/bin/python3
import sys


def process_input(line, stats, size):
    """
    The function `process_input` takes a line of input, updates statistics
    and file size based on the line, and returns the updated file size.

    :param line: The `line` parameter is a string that represents a line of
    input data
    :param stats: The `stats` parameter is a dictionary that stores the count
    of each code encountered in the input. The keys of the dictionary are the
    codes, and the values are the counts
    :param size: The `size` parameter represents the total size of all files
    processed so far
    :return: The variable "size" is being returned.
    """
    try:
        parts = line.split()
        code = int(parts[-2])
        file_size = int(parts[-1])
        size += file_size
        stats[code] = stats.get(code, 0) + 1
    except(IndexError, ValueError):
        pass
    return size


def print_output(stats, size):
    """
    The function `print_output` prints the file size and the statistics in
    a formatted manner.

    :param stats: A dictionary containing statistics about a file. The keys
    of the dictionary represent the type of statistic and the values represent
    the corresponding count of that statistic
    :param size: The `size` parameter represents the file size. It is a value
    that indicates the size of a file in bytes
    """
    print(f"File size: {size}")

    for i in sorted(stats):
        print(f"{i}: {stats[i]}")


if __name__ == "__main__":
    try:
        count = 0
        stats = {}
        size = 0

        for line in sys.stdin:
            count += 1
            size = process_input(line, stats, size)

            if count % 10 == 0:
                print_output(stats, size)

    except KeyboardInterrupt:
        # print_output(stats, size)
        sys.exit()
