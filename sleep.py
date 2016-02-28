#! /bin/env python

import time
import sys
import logging

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    second = float(sys.argv[1])

    if second > 30:
        logging.warning("Sleep too long, abort!")
    else:
        time.sleep(second)
        logging.info("You have slept for {s} seconds.".format(s=second))