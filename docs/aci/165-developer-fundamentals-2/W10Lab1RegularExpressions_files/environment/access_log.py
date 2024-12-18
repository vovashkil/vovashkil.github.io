import re

"""
Regex to parse the log line. You need to have following variables in the groups.

- client IP
- timestamp
- request
- status code
- bytes sent
- referrer
"""
# 192.0.2.18 - - [01/Jan/2023:00:01:00 +0100] "GET /about HTTP/1.1" 404 154122 "https://example.org"
regex = re.compile(r'([\d.]+) - - (\[.*?\]) (\".*?\") (\d{3}) (\d+) (\".*?\")')
"""
In the argument of re.compile(), the regex groups to capture the client IP address and the string "- -" have already been written.

([\d.]+) matches the IP address
- - matches the exact string of two dashes that appears in a server log message
"""

def parse_logfile(logfile):
    """
    Parses the log file and stores the results inside a list of tuples. Each tuple contains the strings that were matched by the regex groups.

    Parameters:
    - logfile(str): log file to parse

    Returns:
    - List[Tuple[str]]
    """
    parsed_lines = []
    with open(logfile, 'r') as f:
        while True:
            line = f.readline().strip()

            # Skip if line is empty
            if not line:
                break

            m = regex.match(line)

            # Skip if line doesn't match the regex
            if not m:
                continue

            parsed_lines.append(m.groups())

    return parsed_lines


def ip_stats(lines):
    """
    Counts the visits per client IP from the parsed log lines, stores them in a dictionary, and prints the top 5 most frequent IP addresses

    Parameters:
    - lines(List[Tuple[str]]): log file lines parsed using regex
    
    Prints:
    - most frequent client IP addresses
    """

    # Create the dictionary that stores the statistics
    ip_hits = dict()
    for line in lines:
        ip = line[0]
        if not ip in ip_hits.keys():
            ip_hits[ip] = 0
        ip_hits[ip] += 1

    # Sort results
    ip_hits = dict(sorted(ip_hits.items(), key=lambda item: item[1], reverse=True))

    # Print the results
    print('Most frequent client IP addresses:')

    for ip in list(ip_hits.keys())[:5]:
        print(f'{ip}: {ip_hits[ip]}')


def page_stats(lines):
    """
    Counts the page visits from the parsed log lines, stores them in a dictionary, and prints the top 5 most visited pages

    Parameters:
    - lines(List[Tuple[str]]): log file lines parsed using regex

    Prints: 
    - most visited pages
    """

    # Create the dictionary that stores the statistics
    page_hits = dict()

    for line in lines:
        # HTTP method and path are together in a single string, but they need to be split into a list of strings
        parts = line[2].split(' ', 3)
        if len(parts) != 3:
            continue
        path = parts[1]

        # Concat host and path
        key = f'{path}'

        if not key in page_hits.keys():
            page_hits[key] = 0
        page_hits[key] += 1

    # Sort results
    page_hits = dict(sorted(page_hits.items(), key=lambda item: item[1], reverse=True))

    # Print the results
    print('\nMost visited pages:')

    for page in list(page_hits.keys())[:5]:
        print(f'{page}: {page_hits[page]}')


def error_stats(lines):
    """
    Counts the number of 4xx and 5xx errors from the parsed log lines, stores them in a dictionary, and prints out their total occurences.

    Parameters:
    - lines(List[Tuple[str]]): log file lines parsed using regex

    Prints:
    - 4xx and 5xx error stats
    """
    
    # Create the dictionary that stores the statistics
    error_stats = {
        '4xx': 0,
        '5xx': 0
    }

    for line in lines:
        status_code:int = int(line[3])
        if status_code >= 400 and status_code < 500:
            error_stats['4xx'] += 1
        elif status_code >= 500:
            error_stats['5xx'] += 1

    # Print the results
    print('\nError count:')

    for code in error_stats.keys():
        print(f'{code}: {error_stats[code]}')


def log_stats(logfile):
    lines = parse_logfile(logfile)
    ip_stats(lines)
    page_stats(lines)
    error_stats(lines)


if __name__ == '__main__':
    log_stats('sample-data/access.log')
