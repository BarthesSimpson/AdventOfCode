import os
from collections import Counter


class Sol:
    def __init__(self, filepath):
        self.filepath = filepath
        self.lines = []

    def solve(self):
        with open(filepath, 'r') as f:
            for line in f:
                self.lines.append(line)

        for i, l1 in enumerate(self.lines[:-1]):
            for l2 in self.lines[i + 1:]:
                if self.levenstein_one(l1, l2):
                    return self.common(l1, l2)

    def levenstein_one(self, l1, l2):
        diff = 0
        for i, c in enumerate(l1):
            if l2[i] != c:
                diff += 1
                if diff > 1:
                    return False
        return diff == 1

    def common(self, l1, l2):
        return ''.join([c for i, c in enumerate(l1) if l2[i] == c])


if __name__ == '__main__':
    dirname = os.path.dirname(__file__)
    INPUT_FILE = './input.txt'
    filepath = os.path.join(dirname, INPUT_FILE)

    print(Sol(filepath).solve())
