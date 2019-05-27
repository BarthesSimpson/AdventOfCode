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
            self.string = self.react(f.read())
        # print(self.string)
        return len(self.string)

    def react(self, polymer):
        L = len(polymer)
        if L == 1 or L == 0:
            return polymer
        elif L == 2:
            if polymer[0] != polymer[1] and polymer[0].upper(
            ) == polymer[1].upper():
                return ''
            else:
                return polymer
        else:
            cut = L // 2
            if polymer[cut - 1] != polymer[cut] and polymer[
                    cut - 1].upper() == polymer[cut].upper():
                return self.combine(self.react(polymer[:cut - 1]),
                                    self.react(polymer[cut + 1:]))
            else:
                return self.combine(self.react(polymer[:cut]),
                                    self.react(polymer[cut:]))

    def combine(self, a, b):
        if a == '' or b == '':
            return a + b
        elif a[-1] != b[0] and a[-1].upper() == b[0].upper():
            return self.combine(a[:-1], b[1:])
        else:
            return a + b


print(Solution(filepath).solve())