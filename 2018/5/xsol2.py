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
            self.string = self.process_string(f.read())
        best = float('inf')
        for c in 'abcdefghijklmnopqrstuvwxyz':
            best = min(
                best,
                len(
                    self.process_string(
                        self.string.replace(c, '').replace(c.upper(), ''))))
        return best

    def process_string(self, string):
        found = True
        while found:
            bitmask = [1] * len(string)
            found = False
            for i in range((len(string) // 2) - 1):
                i1, i2, i3 = (i * 2), (i * 2) + 1, (i * 2) + 2
                c1, c2, c3 = string[i1], string[i2], string[i3]
                if bitmask[i1] and c1 != c2 and c1.upper() == c2.upper():
                    found = True
                    bitmask[i1], bitmask[i2] = 0, 0
                elif c2 != c3 and c2.upper() == c3.upper():
                    found = True
                    bitmask[i2], bitmask[i3] = 0, 0
            string = ''.join(c for i, c in enumerate(string) if bitmask[i])
        return string


print(Solution(filepath).solve())