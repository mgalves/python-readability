import argparse
import sys

from readability_lxml import VERSION
from readability_lxml.readability import Document


def parse_args():
    desc = "fast python port of arc90's readability tool"
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--version',
        action='version', version=VERSION)

    parser.add_argument('-v', '--verbose',
        action='store_true',
        default=False,
        help="Increase logging verbosity to DEBUG.")

    parser.add_argument('path', metavar='P', type=str, nargs=1,
        help="The url or file path to process in readable form.")

    args = parser.parse_args()
    return args


def main():
    args = parse_args()

    target = args.path[0]

    if target.startswith('http') or target.startswith('www'):
        is_url = True
        url = target
    else:
        is_url = False
        url = None

    if is_url:
        import urllib
        target = urllib.urlopen(target)
    else:
        target = open(target, 'rt')

    enc = sys.__stdout__.encoding or 'utf-8'

    try:
        doc = Document(target.read(),
            debug=args.verbose,
            url=url)
        print doc.summary().encode(enc, 'replace')

    finally:
        target.close()


if __name__ == '__main__':
    main()