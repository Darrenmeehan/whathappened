#!/usr/bin/env python3

from whathappened.cli import add_arguments
from whathappened.aws_fun import list_bucket_objects

def main():
    application_handler()


def application_handler():
    parser = add_arguments()
    arguments = parser.parse_args()
    if arguments.sync:
        bucker_name = arguments.bucket_name
        print(f"Syncing {bucker_name} now")

if __name__ == '__main__':
    main()
