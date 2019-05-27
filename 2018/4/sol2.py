import os
import re
from collections import defaultdict, namedtuple

dirname = os.path.dirname(__file__)
INPUT_FILE = './input.txt'
filepath = os.path.join(dirname, INPUT_FILE)

Event = namedtuple('Event', 'year month day hour min guard action')


class Solution:
    def __init__(self, filepath):
        self.filepath = filepath
        self.events = []
        self.by_guard = defaultdict(lambda: defaultdict(int))

    def solve(self):
        self.parse_input()
        self.sort_events()
        for evt in self.events:
            if evt.action != 'Guard':
                assert evt.hour == 0
        self.group_by_guard()
        return self.get_most_habitual()

    def group_by_guard(self):
        guard = None
        falls = None
        i = 0
        for evt in self.events:
            if evt.action == 'Guard':
                guard = evt.guard
            elif evt.action == 'falls':
                falls = evt
            else:
                self.add_record(falls, evt, guard)

    def add_record(self, falls, wakes, guard):
        fall_hr, fall_min = falls.hour, falls.min
        wake_hr, wake_min = wakes.hour, wakes.min
        for _min in range(fall_min, wake_min):
            self.by_guard[guard][_min] += 1

    def get_most_habitual(self):
        _max, _min, g = 0, None, None
        for guard, minutes in self.by_guard.items():
            for minute, count in minutes.items():
                if count > _max:
                    _max, _min, g = count, minute, guard
        return g * _min

    def witching_hour(self, guard):
        g = self.by_guard[guard]
        _max, _min = 0, None
        for minute, count in g.items():
            if count > _max:
                _max, _min = count, minute
        return guard * _min

    def sort_events(self):
        self.events.sort()

    def parse_input(self):
        with open(self.filepath, 'r') as f:
            for line in f:
                parsed = self.parse_line(line)
                if not parsed:
                    return
                self.events.append(Event(*parsed))

    def parse_line(self, line):

        nums = re.findall(r'(\d+)', line)
        action = re.findall(r'\]\s(\w+)', line)
        _nums = [int(n) for n in nums]
        if len(_nums) < 6:
            _nums.append(-1)
        return (*_nums, action[0])


def main():
    print(Solution(filepath).solve())


main()