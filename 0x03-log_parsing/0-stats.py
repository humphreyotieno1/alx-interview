#!/usr/bin/env python3
"""
Log Parsing Script
"""
import re
import sys
from signal import signal, SIGINT


file_size = 0
status_codes = {
    200: 0, 301: 0, 400: 0, 401: 0,
    403: 0, 404: 0, 405: 0, 500: 0
}
line_count = 0


def print_stats(signal_received=None, frame=None):
    """
    Print the summarized log statistics.
    """
    print("File size: {}".format(file_size))
    sorted_codes = sorted(status_codes.keys())
    for code in sorted_codes:
        if status_codes[code]:
            print("{}: {}".format(code, status_codes[code]))


signal(SIGINT, print_stats)


def parse_line(line):
    """
    Parse a single log line and update the metrics.
    """
    global file_size, line_count
    line_pattern = r'^(\d+.\d+.\d+.\d+)' \
                   r' - \[(.+?)\]' \
                   r' "GET \/projects\/260 HTTP\/1.1" (\d+) (\d+)'
    match = re.match(line_pattern, line)
    if not match:
        return

    ip_address, date, status_code, size = match.groups()
    try:
        status_code = int(status_code)
    except ValueError:
        return

    file_size += int(size)
    status_codes[status_code] += 1
    line_count += 1

    if line_count % 10 == 0:
        print_stats()


if __name__ == "__main__":
    try:
        for line in sys.stdin:
            parse_line(line.rstrip())
    except KeyboardInterrupt:
        print_stats()
