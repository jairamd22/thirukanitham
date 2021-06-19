#!/usr/bin/python

import csv
import sys

#input number you want to search
number = "chennai"

#read csv, and split on "," the line
csv_file = csv.reader(open('meta_location.csv', "r"), delimiter=",")


#loop through the csv list
for row in csv_file:
    #if current rows 2nd value is equal to input, print that row
    if number == row[1]:
         print (row)