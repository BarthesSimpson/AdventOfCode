import os
import re
from collections import defaultdict, namedtuple

dirname = os.path.dirname(__file__)
INPUT_FILE = './input.txt'
filepath = os.path.join(dirname, INPUT_FILE)


class Solution:
    def __init__(self, filepath):
        self.filepath = filepath

    def solve(self):
        with open(self.filepath, 'r') as f:
            self.string = f.read()
        self.process_string()
        # print(self.string)
        return len(self.string)

    def process_string(self):
        found = True
        while found:
            bitmask = [1] * len(self.string)
            found = False
            for i in range((len(self.string) // 2) - 1):
                i1, i2, i3 = (i * 2), (i * 2) + 1, (i * 2) + 2
                c1, c2, c3 = self.string[i1], self.string[i2], self.string[i3]
                if bitmask[i1] and c1 != c2 and c1.upper() == c2.upper():
                    found = True
                    bitmask[i1], bitmask[i2] = 0, 0
                elif c2 != c3 and c2.upper() == c3.upper():
                    found = True
                    bitmask[i2], bitmask[i3] = 0, 0
            self.string = ''.join(c for i, c in enumerate(self.string)
                                  if bitmask[i])


print(Solution(filepath).solve())