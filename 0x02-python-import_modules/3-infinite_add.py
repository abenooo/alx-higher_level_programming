#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    index = 1
    sum = 0
    for index in range(1, len(sys.argv)):
        sum += int(sys.argv[index])
    print(sum)
