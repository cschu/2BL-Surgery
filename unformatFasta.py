#!/usr/bin/env python
import sys

def readFasta(fn):
    head, seq = None, ''
    with open(fn) as fi:
        for line in fi:
            if line[0] == '>':
                if head is not None:
                    yield (head, seq)
                head, seq = line.strip().strip('>'), ''
            else:
                seq += line.strip()
        yield (head, seq)

def main(argv):
    for head, seq in readFasta(argv[0]):
        sys.stdout.write('>%s\n%s\n' % (head, seq))


if __name__ == '__main__': main(sys.argv[1:])
