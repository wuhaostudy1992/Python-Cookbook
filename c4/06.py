from collections import deque

class linehistory:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            print("history:{}".format(self.history))
            yield line

    def clear(self):
        self.history.clear()

with open('test.txt') as f:
    lines = linehistory(f)
    for line in lines:
        if 'the' in line:
            for lineno, line in lines.history:
                print('{}:{}'.format(lineno, line))
