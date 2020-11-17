"""
Commandline Setup.
"""
import argparse


def add_arguments():
    sync_parser = argparse.ArgumentParser(add_help=False)
    sync_parser.add_argument("sync")

    bucket_parser = argparse.ArgumentParser(parents=[sync_parser])
    bucket_parser.add_argument("--bucket-name", required=True, action="store")
    return bucket_parser