#!/usr/bin/python

import sys
from subprocess import Popen, PIPE
import yaml

config_file = '/path/to/source/file'


def get_data():
    """
    Read config file and load into a list of dicts
    """
    listChoices = []
    with open(config_file, 'r') as f:
        options = yaml.safe_load(f)
    for entry, data in options.items():
        """
        This is a very hacky method of getting proper spacing
        so the tags don't show up one the same line
        """
        whitespace = 100
        description = data.get('description').ljust(whitespace, ' ')
        tags = str(data.get('tags', ''))[1:-1].rjust(whitespace, ' ')
        listChoices.append({'url': entry, 'choice': description + tags})
    return(listChoices)


if __name__ == '__main__':
    data = get_data()

    if len(sys.argv) > 1:
        """
        If a selection is made, copy the URL to the system clipboard
        """
        choice = next((item for item in data if item['choice'] == sys.argv[1]))
        Popen(('xsel', '-ib'), stdin=PIPE ).communicate(str.encode(choice['url']))
        sys.exit()
    else:
        """
        Populate the list of choices
        """
        for entry in data:
            print(entry['choice'])
