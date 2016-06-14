#!/usr/bin/env python
# coding: utf-8


from __future__ import print_function
from smb.SMBHandler import SMBHandler
import urllib
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
            urllib.parse.quote(args.domain, safe=''),
            urllib.parse.quote(args.username, safe=''),
            urllib.parse.quote(args.password, safe=''),
            urllib.parse.quote(args.host, safe=''),
            args.PATH
    )

    director = urllib.request.build_opener(SMBHandler)
    fh = director.open(url)

    outfile = args.DEST if args.DEST else ntpath.basename(args.PATH)

    with open(outfile, 'wb') as out:
        for line in fh:
            out.write(line)
    fh.close()
