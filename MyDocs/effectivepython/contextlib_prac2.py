import logging
from contextlib import contextmanager

@contextmanager
def log_level(level, name):
    logger = logging.getLogger(name)
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield logger
    finally:
        logger.setLevel(old_level)


def main():
    with log_level(logging.DEBUG, 'my-log') as logger:
        logger.debug('This is my message!')
        logging.debug('This will not print')

    print()
    logger = logging.getLogger('my-log')
    logger.debug('Debug will not print')
    logger.error('Error will print')


if __name__ == '__main__':
    main()