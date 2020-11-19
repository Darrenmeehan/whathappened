#!/usr/bin/env python3
"""
Set of this file somewhat changed based on some learnigs from the following -
https://chriswarrick.com/blog/2014/09/15/python-apps-the-right-way-entry_points-and-scripts/
"""

import sys

# from whathappened.whathappened.cli import add_arguments
from whathappened.cli import add_arguments
from whathappened.aws_fun import list_bucket_objects


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    parser = add_arguments()
    arguments = parser.parse_args()
    if arguments.sync:
        bucker_name = arguments.bucket_name
        print(f"Syncing {bucker_name} now")


if __name__ == "__main__":
    sys.exit(main())
