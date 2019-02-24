import logging
from contextlib import contextmanager


def my_function():
    logging.debug('Some debug data')
    logging.error('Error log here')
    logging.debug('More debug data')

@contextmanager
def debug_logging(level):
    logger = logging.getLogger()
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield
    finally:
        logger.setLevel(old_level)


def main():
    with debug_logging(logging.DEBUG):
        print('Inside')
        my_function()
    print('Outside')
    my_function()


if __name__ == '__main__':
    main()