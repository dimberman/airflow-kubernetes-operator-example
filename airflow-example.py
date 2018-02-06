import sys


def fail():
    return 10 / 0


def succeed():
    return 10 / 1


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: wordcount <file>", file=sys.stderr)
        exit(-1)
    arg = sys.argv[1]
    if arg == 'pass':
        succeed()
    elif arg == 'fail':
        fail()
    else:
        print('invalid command: {}'.format(arg))
        exit(-1)
