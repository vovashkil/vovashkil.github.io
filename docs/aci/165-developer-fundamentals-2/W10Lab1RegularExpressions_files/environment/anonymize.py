import re


#regex_name = r'"name": "(\w+? \w*? \w+)"'
regex_name = r'"name": "([\w\s]+)"'

#regex_email = r'"email": "(\w+@\w\.\w+)"'
regex_email = r'"email": "(\S+@\S+\.\S+)"'


def anonymize_file(filename, output_filename):
    """
    Creates new file with anonymous data

    Parameters:
    - filename(str): input filename
    - output_filename(str): output filename
    
    Returns:
    - None
    """
    with open(output_filename, 'w+') as f_out:
        with open(filename, 'r') as f_in:
            # Read whole file into a string
            file_contents = ''.join(f_in.readlines())

            # Anonymize e-mail
            # re.sub() replaces all occurrences of a pattern with the value of the repl parameter.
            file_contents = re.sub(pattern=regex_email,
                                   repl='"email": "REDACTED@example.com"',
                                   string=file_contents,
                                   flags=re.MULTILINE | re.IGNORECASE)

            # Anonymize name
            file_contents = re.sub(pattern=regex_name,
                                   repl='"name": "REDACTED"',
                                   string=file_contents,
                                   flags=re.MULTILINE | re.IGNORECASE)

            # Write the output file
            f_out.write(file_contents)


if __name__ == '__main__':
    anonymize_file('sample-data/people.dat', 'people-anonymized.dat')
