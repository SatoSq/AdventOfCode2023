# -*- coding: utf-8 -*-
"""
2023-12-01

@author: Sato

----- AdventOfCode2023 ------
--- Day 1: Trebuchet?! ---
"""


numbers = ['zero','one','two','three','four','five','six','seven','eight','nine']
#'zero' added so index == digit value

def extract_str_digits(line):
    digits=[]
    for i in numbers:
        if i in line:
            digits+=[[line.find(i), numbers.index(i)]]+[[line.rfind(i), numbers.index(i)]]
    return digits

def calibrate(line, part):
    if part==2:
        value=extract_str_digits(line)
    else:
        value=[]
    for i in line:
        try:
            value+=[[line.index(i), int(i)]]+[[line.rindex(i), int(i)]]
        except:
            pass
    value.sort()


    calibration_value = str(value[0][1]) + str(value[-1][1])
    return calibration_value



def main(part):
    f = open('1.txt', 'r')
    line=[0]
    sum=0
    c = 1
    while c:
        line=f.readline()
        try:
            calibration_value = calibrate(line, part)
            sum+= int(calibration_value)
        except:
            c = 0
    f.close()
    return sum

print(extract_str_digits("zoneight234"))
print(calibrate("zoneight234",2))
print("Part1:",main(1))
print("Part2:",main(2))
