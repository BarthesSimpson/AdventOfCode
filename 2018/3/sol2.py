import os
import re
import os
import re
from collections import Counter

dirname = os.path.dirname(__file__)
INPUT_FILE = './input.txt'
filepath = os.path.join(dirname, INPUT_FILE)


def main():
    with open(filepath, 'r') as f:
        claims = [[*map(int, re.findall(r'\d+', l))] for l in f if l]
        squares = lambda c: ((i, j) for i in range(c[1], c[1] + c[3])
                             for j in range(c[2], c[2] + c[4]))
        fabric = Counter(s for c in claims for s in squares(c))

        return next(c[0] for c in claims
                    if all(fabric[s] == 1 for s in squares(c)))


print(main())
