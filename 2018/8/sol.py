import os
import sys

dirname = os.path.dirname(__file__)
INPUT_FILE = './input.txt'
filepath = os.path.join(dirname, INPUT_FILE)

class Solution:
    def __init__(self, filepath):
        self.filepath = filepath
        self.graph = None

    def solve(self):
        self.parse_input()
        return self.calculate_sum(self.graph)

    def parse_input(self):
        with open(self.filepath, 'r') as f:
            self.graph = list(map(int, f.read().split(' ')))

    def calculate_sum(self, data):
        children, metas = data[:2]
        data = data[2:]
        scores = []
        totals = 0

        for i in range(children):
            total, score, data = self.calculate_sum(data)
            totals += total
            scores.append(score)

        totals += sum(data[:metas])

        if children == 0:
            return (totals, sum(data[:metas]), data[metas:])
        else:
            return (totals,
                    sum(scores[k - 1] for k in data[:metas]
                        if k > 0 and k <= len(scores)), data[metas:])


print(Solution(filepath).solve())
