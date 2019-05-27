import os
import re
import sys
import numpy as np
import bisect
from collections import defaultdict
from matplotlib import pyplot as plt

dirname = os.path.dirname(__file__)
INPUT_FILE = './input.txt'
filepath = os.path.join(dirname, INPUT_FILE)


class Solution:
    def __init__(self, filepath, threshold):
        self.filepath = filepath
        self.sorted_by_x = []
        self.valid_region = 0
        self.threshold = threshold

    def solve(self):
        with open(self.filepath, 'r') as f:
            for line in f:
                x, y = re.findall(r'\d+', line)
                bisect.insort(self.sorted_by_x, (int(x), int(y)))
        self.set_boundaries()
        self.compute_coverage()
        return self.valid_region

    def set_boundaries(self):
        self.min_x = self.sorted_by_x[0][0]
        self.max_x = self.sorted_by_x[-1][0]
        self.min_y, self.max_y = float('inf'), 0
        for x, y in self.sorted_by_x:
            self.min_y = min(self.min_y, y)
            self.max_y = max(self.max_y, y)

    def compute_coverage(self):
        count = 0
        for x1 in range(self.min_x, self.max_x + 1):
            for y1 in range(self.min_y, self.max_y + 1):
                count += 1
                is_valid = self.test_point((x1, y1))
                if is_valid:
                    self.valid_region += 1

    def test_point(self, point):
        x1, y1 = point
        total = 0
        for x2, y2 in self.sorted_by_x:
            dist = self.manhattan_distance(x1, y1, x2, y2)
            total += dist
            if total > self.threshold:
                return False
        return True

    def manhattan_distance(self, x1, y1, x2, y2):
        return abs(x2 - x1) + abs(y2 - y1)

    def get_max_coverage(self):
        candidates = sorted(self.areas.items(),
                            key=lambda x: x[1],
                            reverse=True)
        for candidate, count in candidates:
            if not self.is_infinite(candidate):
                return count

    def is_infinite(self, point):
        x, y = point
        x_boundary = self.max_x if x > self.max_x // 2 else self.min_x
        y_boundary = self.max_y if y > self.max_y // 2 else self.min_y
        nearest_at_x = self.get_nearest_points((x_boundary, y))
        if len(nearest_at_x) == 1 and nearest_at_x[0] == point:
            return True
        nearest_at_y = self.get_nearest_points((x, y_boundary))
        if len(nearest_at_y) == 1 and nearest_at_y[0] == point:
            return True
        return False


print(Solution(filepath, 10000).solve())
