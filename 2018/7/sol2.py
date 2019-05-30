import os
import re
import sys
import heapq
from collections import defaultdict

dirname = os.path.dirname(__file__)
INPUT_FILE = './input.txt'
filepath = os.path.join(dirname, INPUT_FILE)


class Solution:
    def __init__(self, filepath, num_workers):
        self.filepath = filepath
        self.graph = defaultdict(set)
        self.num_workers = num_workers

    def solve(self):
        with open(self.filepath, 'r') as f:
            for line in f:
                _, head, tail = re.findall(r'[A-Z]', line)
                self.graph[tail].add(head)
                if not head in self.graph:
                    self.graph[head] = set()

        self.toposort()
        return self.elapsed

    def toposort(self):
        to_add = []
        in_progress = []
        visited = set()
        self.elapsed = 0
        while self.graph:
            for vertex, edges in self.graph.items():
                if vertex not in visited and not edges:
                    heapq.heappush(to_add, vertex)
                    visited.add(vertex)            

            while to_add and len(in_progress) < self.num_workers:
                next_vertex = heapq.heappop(to_add)
                in_progress.append(
                    (61 + ord(next_vertex) - ord('A'), next_vertex))
                    
            wait, done = min(in_progress)
            self.elapsed += wait
            in_progress = [(time - wait, task)
                            for time, task in in_progress
                            if task is not done]
            self.delete(done)

    def delete(self, vertex):
        if vertex in self.graph:
            del self.graph[vertex]
        for _, edges in self.graph.items():
            if vertex in edges:
                edges.remove(vertex)


print(Solution(filepath, 6).solve())
