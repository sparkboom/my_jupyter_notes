import re

def count_magic2(line, cell):
    content = re.sub('[^A-Za-z0-9\s]', ' ', cell)
    content = re.sub('\s+', ' ', content)
    return len(content.lower().split(' '))

def load_ipython_extension(ipython):
    ipython.register_magic_function(count_magic2, 'cell')
    