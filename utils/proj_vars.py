# -*- coding: utf-8 -*-
import pygit2
import os
import socket


PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

HOSTNAME = socket.gethostname()


repo = pygit2.Repository(os.path.join(PROJECT_DIR, '.git'))

CODE_BRANCH = repo.head.shorthand
CODE_VERSION = repo.head.target


if __name__ == '__main__':
    print('PROJECT_DIR: %s' % PROJECT_DIR)
    print('HOSTNAME: %s' % HOSTNAME)
    print('CODE_BRANCH: %s' % CODE_BRANCH)
    print('CODE_VERSION: %s' % CODE_VERSION)
