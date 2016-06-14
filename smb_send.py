#!/usr/bin/env python
# coding: utf-8


from __future__ import print_function
from smb.SMBHandler import SMBHandler
import urllib
import argparse
import ntpath
import logging


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
    dest_path = ntpath.join(args.DEST, ntpath.basename(args.FILE.name))
    logger.info('Transfering {} to {}'.format(args.FILE.name, dest_path))

    url = 'smb://{};{}:{}@{}/{}'.format(
        urllib.parse.quote(args.domain, safe=''),
        urllib.parse.quote(args.username, safe=''),
        urllib.parse.quote(args.password, safe=''),
        urllib.parse.quote(args.host, safe=''),
        dest_path
    )

    director = urllib.request.build_opener(SMBHandler)
    fh = director.open(url, data=args.FILE)
    fh.close()
