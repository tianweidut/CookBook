#coding: utf-8

import sys
import os
import logging


def main():
    s_o = os.dup(1)
    s_e = os.dup(2)
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s %(message)s")
    logging.info('init')
    print os.environ.get('PYTHONUNBUFFERED')
    os.environ['PYTHONUNBUFFERED'] = '1'

    fd = os.open('test.log', os.O_RDWR | os.O_CREAT)
    os.dup2(fd, 1)
    os.dup2(fd, 2)

    print 'out1'
    print >> sys.stderr, 'err1'
    logging.info('init-1')
    reload(sys)
    print >> sys.stderr, os.environ.get('PYTHONUNBUFFERED')
    logging.info('initi-2')
    print 'out2'
    print >> sys.stderr, 'err2'

    os.dup2(s_o, 1)
    os.dup2(s_e, 2)

    print 'finish, err'
    print >> sys.stderr, 'finish err'
    logging.info('end')


if __name__ == "__main__":
    main()
