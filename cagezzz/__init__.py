import random
import threading
import time
import sys
from pkg_resources import resource_filename

__version__ = '0.0.1'

def generate_the_cagezzz():
    """
    Function to parse the image file and generate a list of cagezzz
    for display
    """
    with open(resource_filename('cagezzz','cagezzz.txt'), 'r') as f:
        lines = f.readlines()
    cagezzzs = []
    cagezzz  = []
    for line in lines:
        if not line.strip(): #images seperated by a newline
            cagezzzs.append(''.join(cagezzz))
            cagezzz = []
        else:
            cagezzz.append(line)
    return cagezzzs


def release_the_cagezzz():
    """
    Display the cagezzz at random intervals
    """
    cagezzz = generate_the_cagezzz()

    n_cage = random.randint(1, 10)
    for _ in range(n_cage):
        time.sleep(random.randint(5, 15))
        print('\n' + random.choice(cagezzz) + '\n')

    del sys.modules['cagezzz']

thread = threading.Thread(target=release_the_cagezzz)
thread.daemon = True
thread.start()
