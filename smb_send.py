#!/usr/bin/env python
# coding: utf-8


from __future__ import print_function
from easypysmb import EasyPySMB
import argparse
import logging
import os


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--domain', required=True, help='Domain name')
    parser.add_argument('-H', '--host', required=True, help='SMB host')
    parser.add_argument('-u', '--username', required=True, help='Username')
    parser.add_argument('-p', '--password', required=True, help='Password')
    parser.add_argument(
        'FILE', type=argparse.FileType('rb'), help='File to transfer'
    )
    parser.add_argument(
        'DEST',
        nargs='?',
        help='Destination (where to put the file)'
    )
    args = parser.parse_args()
    dest_path = os.path.join(args.DEST, os.path.basename(args.FILE.name))
    logger.info('Transfering {} to {}'.format(args.FILE.name, dest_path))

    url = 'smb://{};{}:{}@{}/{}'.format(
        args.domain,
        args.username,
        args.password,
        args.host,
        dest_path
    )

    e = EasyPySMB(url)
    e.store_file(args.FILE)
