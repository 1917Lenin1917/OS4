from functools import reduce 
from sys import argv

def f(size: int, b: int, c: int):
    return reduce(lambda a, i: a + b * 2 + c - i, range(size), 0)


def main():
    if len(argv) != 5: 
        return -1
    
    size = int(argv[1])
    b    = int(argv[2])
    c    = int(argv[3])
    repeat_times = int(argv[4])

    for i in range(repeat_times):
        value = f(size, b, c)


if __name__ == '__main__':
    main()
