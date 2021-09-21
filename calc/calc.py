import re

def add(num):
    if num == '':
        return 0

    num = map(int, re.findall(r"-?\d+", num))
    num = filter(lambda x: x < 1000, num)
    return sum(num)