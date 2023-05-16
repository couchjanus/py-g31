# ======================6==============================
# Написати скрипт виводу квадрата заданого числа
# Використовуючи модуль argparse, додати до скрипта підказку
# при виклику програми: python prog.py --help

# потрібно отримати такий результат:

# usage: square.py [-h] [-v] square

# positional arguments:
#   square         display a square of a given number

# options:
#   -h, --help     show this help message and exit
#   -v, --verbose  increase output verbosity

import argparse 

parser = argparse.ArgumentParser()

parser.add_argument("square", type=int,
                    help="display a square of a given number")

parser.add_argument("-v", "--verbose", action="store_true",
                    help="increase output verbosity")

args = parser.parse_args()

answer = args.square**2

if args.verbose:
    print(f"the square of {args.square} equals {answer}")
else:
    print(answer)