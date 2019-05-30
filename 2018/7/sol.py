import os
import re
import sys
import heapq
from collections import defaultdict

dirname = os.path.dirname(__file__)
INPUT_FILE = './input.txt'
filepath = os.path.join(dirname, INPUT_FILE)


class Solution:
    def __init__(self, filepath):
        self.filepath = filepath
        self.graph = defaultdict(set)
        self.path = []

    def solve(self):
        with open(self.filepath, 'r') as f:
            for line in f:
                _, head, tail = re.findall(r'[A-Z]', line)
                self.graph[tail].add(head)
                if not head in self.graph:
                    self.graph[head] = set()

        # print(self.graph)
        self.toposort()
        return ''.join(self.path)

    def toposort(self):
        to_add = []
        while self.graph:
            for vertex, edges in self.graph.items():
                if not edges:
                    heapq.heappush(to_add, vertex)
            visited = set(to_add)
            while to_add:
                next_vertex = heapq.heappop(to_add)
                self.path.append(next_vertex)
                self.delete(next_vertex)
                for vertex, edges in self.graph.items():
                    if vertex not in visited and not edges:
                        heapq.heappush(to_add, vertex)
                        visited.add(vertex)


    def delete(self, vertex):
        if vertex in self.graph:
            del self.graph[vertex]
        for _, edges in self.graph.items():
            if vertex in edges:
                edges.remove(vertex)



print(Solution(filepath).solve())
