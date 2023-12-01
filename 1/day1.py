# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 12:44:30 2023

@author: Sato

AdventOfCode2023: day 1
"""

def calibrate(line):
    value=[]
    for i in line:
        try: 
            value+= [int(i)]
        except:
            pass

    calibration_value = str(value[0]) + str(value[-1])
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