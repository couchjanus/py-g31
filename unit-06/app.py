import sys

# print(f'sys.argv : {sys.argv}')
# print(f'type sys.argv : {type(sys.argv)}')
# print(f'len sys.argv : {len(sys.argv)}')

# print(sys.maxsize)
# sys.exit('Error msg')
# print(sys.path)
# print(sys.version)

import os

# with os.scandir('files/') as items:
#     for item in items:
#         print(item.name)

# import pathlib
from pathlib import Path

# Path.touch('./libs/test.lib')
# file_name = Path('./libs/test1.lib')
# if not file_name.exists():
#     Path.touch(file_name)

# (walrus := True)
# print(walrus)

x = 3
# print(f'{x:=8}')
# print(f'{(x := 8)}')

# number = 3

# if square := number**2 > 5:
#     print(square)

# if (square := number**2) > 5:
#     print(square)

# if (args_count := len(sys.argv)) > 2:
#     print(f'One argumen expected, got {args_count - 1}')
#     raise SystemExit(2)
# elif args_count < 2:
#     print(f'You must specify the target directory')
#     raise SystemExit(2)

# target_dir = Path(sys.argv[1])

# if not target_dir.is_dir():
#     print(f'The target directory doesn\'t exist')
#     raise SystemExit(1)

# for item in target_dir.iterdir():
#     print(item.parent,'/', item.name)
    
import argparse

# parser = argparse.ArgumentParser()

# parser.add_argument("path")
# args = parser.parse_args()

# target_dir = Path(args.path)

# if not target_dir.exists():
#     print(f'The target directory doesn\'t exist')
#     raise SystemExit(1)

# for item in target_dir.iterdir():
#     print(item.name)
    

import time

print(time.time())
print(time.ctime(time.time()))

import calendar

# print(calendar.calendar(2023))

import datetime

# date1 = datetime.datetime(2023, 5, 11, 20, 30, 0)
# print(date1.weekday())

# parser = argparse.ArgumentParser(prog="lists")

# parser = argparse.ArgumentParser(
#     prog="lists",
#     description="List the content of a directory",
#     epilog="Thanks for using %(prog)s! :)",
#     )

# parser.add_argument("path")
# parser.add_argument("-l", "--long", action="store_true")
# args = parser.parse_args()

# target_dir = Path(args.path)

# if not target_dir.exists():
#     print(f'The target directory doesn\'t exist')
#     raise SystemExit(1)

# def build_output(entry, long=False):
#     if long:
#         size = entry.stat().st_size
#         date = datetime.datetime.fromtimestamp(
#             entry.stat().st_mtime).strftime(
#                 "%b %d %H:%M:%S"
#         )
#         return f"{size:>6d} {date} {entry.name}"
    
#     return entry.name

# for item in target_dir.iterdir():
#     print(build_output(item, long=args.long))

parser = argparse.ArgumentParser(
    prog="lists",
    description="List the content of a directory",
    epilog="Thanks for using %(prog)s! :)",
    )
general = parser.add_argument_group("general output")
general.add_argument(
    "path",
    nargs="?",
    default=".",
    help="take the path to target directory (default: %(default)s)",
)
detailed = parser.add_argument_group("detailed output")
detailed.add_argument(
    "-l",
    "--long",
    action="store_true",
    default=".",
    help="display detailed diretory content",
)
parser.add_argument("path")
# parser.add_argument("-l", "--long", action="store_true")
args = parser.parse_args()
target_dir = Path(args.path)

if not target_dir.exists():
    print(f'The target directory doesn\'t exist')
    raise SystemExit(1)

def build_output(entry, long=False):
    if long:
        size = entry.stat().st_size
        date = datetime.datetime.fromtimestamp(
            entry.stat().st_mtime).strftime(
                "%b %d %H:%M:%S"
        )
        return f"{size:>6d} {date} {entry.name}"
    
    return entry.name

for item in target_dir.iterdir():
    print(build_output(item, long=args.long))