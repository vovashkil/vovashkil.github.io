import re
from datetime import datetime

"""
You will write regex groups to match the following sections from a server log line:
- month
- day
- time
- queue ID
- message
"""

#regex = re.compile(r'(\w{3}) (\d{1,2})')
regex = re.compile(r'(\w{3}) (\d{1,2}) (\d{1,2}:\d{1,2}:\d{1,2}) mail postfix\/\w+\[\d+\]: ([A-F0-9]{10}): (.*)')
"""
In the argument of re.compile, the regex groups to capture the month and day have already been filled out.

(\w{3}) matches the month, such as 'Jan'
(\d{1,2}) matches the day, such as '14'
"""


# The following functions are used to generate statistics for the server log entries, and print them out in the terminal.

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


def get_line_timestamp(line):
    """
    Converts a log entry's month, day, and time into a datetime instance

    Parameters:
    - line(Tuple[str]): parsed log line

    Returns:
    - datetime
    """
    return datetime.strptime(f'{line[0]} {line[1]} {line[2]}', '%b %d %H:%M:%S')     


def postfix_stats(lines):
    """
    Iterates through the parsed log lines, creating a dictionary to store timestamps for each unique queue ID. 
    Calculates the time difference between "message-id" and "status=sent" timestamps for each ID, and prints the time taken to send the corresponding email.

    Parameters:
    - lines(List[Tuple[str]]): log file lines parsed using regex

    Prints:
    - the statistics gathered from the email logs (postfix is the name of the email server software).
    """
    
    # Create the dictionary that stores the statistics
    stats = dict()

    for line in lines:
        queue_id = line[3]

        if queue_id not in stats.keys():
            stats[queue_id] = {
                'in': None,
                'out': None
            }
        
        # Check message-id, and store the timestamp
        if 'message-id' in line[4]:
            stats[queue_id]['in'] = get_line_timestamp(line)

        # Check status sent, and store the timestamp
        if 'status=sent' in line[4]:
            stats[queue_id]['out'] = get_line_timestamp(line)           

    # Print the results
    print('Email queue stats:')

    for queue_id in stats.keys():
        # Skip if no data is found for given queue ID
        if stats[queue_id]['in'] is None or stats[queue_id]['out'] is None:
            continue
        
        # Calculate the difference in time
        delta = stats[queue_id]['out'] - stats[queue_id]['in']

        print(f'[{queue_id}] sent in {delta.seconds} seconds')


if __name__ == '__main__':
    lines = parse_logfile('sample-data/mail.log')
    postfix_stats(lines)
