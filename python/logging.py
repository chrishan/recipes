import logging
import optparse

# By default, the logging module prints critical, error and warning messages. To change this so that all levels are printed, use:
# $ ./your-program.py --logging=debug
# To send log messages to a file called debug.log, use:
# $ ./your-program.py --logging-level=debug --logging-file=debug.log


LOGGING_LEVELS = {'critical': logging.CRITICAL,
                  'error': logging.ERROR,
                  'warning': logging.WARNING,
                  'info': logging.INFO,
                  'debug': logging.DEBUG}


def main():
    parser = optparse.OptionParser()
    parser.add_option('-l', '--logging-level', help='Logging level')
    parser.add_option('-f', '--logging-file', help='Logging file name')
    (options, args) = parser.parse_args()
    logging_level = LOGGING_LEVELS.get(options.logging_level, logging.NOTSET)
    logging.basicConfig(level=logging_level, filename=options.logging_file,
                        format='%(asctime)s %(levelname)s: %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    # Your program goes here.
    # You can access command-line arguments using the args variable.

if __name__ == '__main__':
    main()
