import os
import sys
import re
from collections import defaultdict, deque

dirname = os.path.dirname(__file__)
INPUT_FILE = './input2.txt'
filepath = os.path.join(dirname, INPUT_FILE)


class Solution:
    def __init__(self, filepath):
        self.filepath = filepath
        self.scores = defaultdict(int)

    def solve(self):
        self.parse_input()
        self.circle = deque([0])
        for marble in range(1, self.final_marble + 1):
            if marble % 23 == 0:
                self.circle.rotate(7)
                self.scores[marble %
                            self.num_players] += marble + self.circle.pop()
                self.circle.rotate(-1)
            else:
                self.circle.rotate(-1)
                self.circle.append(marble)
        return max(self.scores.values())

    def parse_input(self):
        with open(self.filepath, 'r') as f:
            self.num_players, self.final_marble = map(
                int, re.findall(r'(\d+)', f.read()))


print(Solution(filepath).solve())
