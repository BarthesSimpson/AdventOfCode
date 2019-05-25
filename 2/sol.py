import os
from collections import Counter

class Sol:
    def __init__(self, filepath):
        self.filepath = filepath
        self.twos = 0
        self.threes = 0

    def solve(self):
        with open(filepath, 'r') as f:
            for line in f:
                self.process(line)

        return self.twos * self.threes

    def process(self, label):
        c = Counter(label)
        if 2 in c.values():
            self.twos += 1
        if 3 in c.values():
            self.threes += 1

if __name__ == '__main__':
    dirname = os.path.dirname(__file__)
    INPUT_FILE = './input.txt'
    filepath = os.path.join(dirname, INPUT_FILE)

    print(Sol(filepath).solve())
