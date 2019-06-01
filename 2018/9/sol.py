import os
import sys
import re
from collections import defaultdict

dirname = os.path.dirname(__file__)
INPUT_FILE = './input.txt'
filepath = os.path.join(dirname, INPUT_FILE)


class Solution:
    def __init__(self, filepath):
        self.filepath = filepath
        self.scores = defaultdict(int)

    def solve(self):
        self.parse_input()
        print(self.num_players, self.final_marble)
        self.circle = [0]
        self.current_player = 0
        self.current_marble = 1
        for i in range(1, self.final_marble + 1):
            self.make_move(i)

    def make_move(self, i):
        """
        Check self.current_player to see who's playing
        Check self.current_marble to see where to insert
        Check the rules to see whether to insert and how
        to update the grid and self.scores[current_player]
        """
        pass

    def parse_input(self):
        with open(self.filepath, 'r') as f:
            self.num_players, self.final_marble = map(
                int, re.findall(r'(\d+)', f.read()))


print(Solution(filepath).solve())
