import logging

# enable info logging
logging.basicConfig(level=logging.INFO)

# Formatter example
FORMAT = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.basicConfig(format=FORMAT)
d = {'name': 'John', 'age': 23}

logging.warning('Watch out!')
logging.info('I told you so %s', d)
