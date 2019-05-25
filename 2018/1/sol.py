import os


def main():
    dirname = os.path.dirname(__file__)
    INPUT_FILE = './input.txt'
    filepath = os.path.join(dirname, INPUT_FILE)
    freq = 0
    with open(filepath, 'r') as f:
        for line in f:
            op = line[0]
            if op == '+':
                freq += int(line[1:])
            else:
                freq -= int(line[1:])
    return freq


print(main())
