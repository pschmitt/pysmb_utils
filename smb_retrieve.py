#!/usr/bin/env python
# coding: utf-8


from __future__ import print_function
from easypysmb import EasyPySMB
import argparse
import ntpath


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--domain', help='Domain name')
    parser.add_argument('-H', '--host', help='SMB host')
    parser.add_argument('-u', '--username', help='Username')
    parser.add_argument('-p', '--password', help='Password')
    parser.add_argument('PATH', help='Path to the file to fetch')
    parser.add_argument(
        'DEST',
        nargs='?',
        help='Destination (where to put the file)'
    )
    args = parser.parse_args()

    url = 'smb://{};{}:{}@{}/{}'.format(
        args.domain,
        args.username,
        args.password,
        args.host,
        args.PATH
    )

    e = EasyPySMB(url)

    outfilename = args.DEST if args.DEST else ntpath.basename(args.PATH)

    with open(outfilename, 'wb') as out:
        e.retrieve_file(file_obj=out)
