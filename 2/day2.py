# -*- coding: utf-8 -*-
"""
2023-12-02

@author: Sato

----- AdventOfCode2023 ------
--- Day 2: Cube Conundrum ---
"""

import re

colors=['green', 'red', 'blue']
bag = [13,12,14]

def max_color(line, c):      #maximum value for a given color 'c' within a line
    values = re.findall(r'(\d+) ' + c, line)   #<3 regex (no)
    values = list(map(int, values))
    try:
        m=max(values)
    except:
        m=0
    return m

def game(line,bag):
    for c in range(3):
        if max_color(line,colors[c]) > bag[c]:
            return 0
    return int(re.search(r"\d+", line).group())

def part1():
    bag = [13,12,14]
    f = open('2.txt', 'r')
    line=[0]
    sum=0
    c=1
    while c:
        try:
            line=f.readline()
            sum += game(line,bag)
        except:
            c = 0
    f.close()
    return sum


def part2():
    f = open('2.txt', 'r')
    line=[0]
    sum=0
    c=0
    while c<=100:
        line=f.readline()
        power=1
        for i in colors:
            power*=max_color(line,i)
        sum += power
        c+=1

    f.close()
    return sum

print("Part 1:", part1())
print("Part 2:", part2())
