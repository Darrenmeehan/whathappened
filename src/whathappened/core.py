#!/usr/bin/env python3
"""
Set of this file somewhat changed based on some learnings from the following -
https://chriswarrick.com/blog/2014/09/15/python-apps-the-right-way-entry_points-and-scripts/
"""

import sys

from whathappened.aws_fun import sync_bucket
from whathappened.cli import add_arguments


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    parser = add_arguments()
    arguments = parser.parse_args(args)
    if arguments.sync:
        bucket_name = arguments.bucket_name
        print(f"Syncing {bucket_name} now")
        sync_bucket(bucket_name)


if __name__ == "__main__":
    sys.exit(main())
