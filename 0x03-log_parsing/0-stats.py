#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics"""
import sys


if __name__ == "__main__":
    count = 0
    stats = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    size = 0

    def print_output():
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
            if stats[i]:
                print(f"{i}: {stats[i]}")


    try:
        for line in sys.stdin:
            count += 1
            try:
                parts = line.split(" ")
                code = int(parts[-2])
                file_size = int(parts[-1])
            except(IndexError, ValueError):
                continue
            size += file_size
            stats[code] += 1

            if count % 10 == 0:
                print_output()
        print_output()
    except KeyboardInterrupt:
        print_output()
