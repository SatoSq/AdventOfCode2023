# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 12:44:30 2023

@author: Sato

AdventOfCode2023: day 1
"""

numbers = ['zero','one','two','three','four','five','six','seven','eight','nine']
#'zero' added so index == digit value

def extract_str_digits(line):
    digits=[]
    for i in numbers:
        if i in line:
            digits+=[[line.find(i), numbers.index(i)]]+[[line.rfind(i), numbers.index(i)]]
    return digits

def calibrate(line):
    value=extract_str_digits(line)
    for i in line:
        try: 
            value+=[[line.index(i), int(i)]]+[[line.rindex(i), int(i)]]
        except:
            pass
    value.sort()
    

    calibration_value = str(value[0][1]) + str(value[-1][1])
    return calibration_value

    

def main(): 
    f = open('1.txt', 'r')  
    line=[0]
    sum=0
    c = 1
    while c:
        line=f.readline()
        try:
            calibration_value = calibrate(line)
            sum+= int(calibration_value)
        except:
            c = 0
    f.close()
    return sum