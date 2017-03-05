#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This program DOES SOME STUFF.
"""


import csv
import time
from server import *
from request import *
from queue import *

file_data = raw_input("Enter filename: ")

input_file = file_data.split()
output_file = open("testdata.csv", "w")


    for line in input_file:
        output_file.write(line)
        output_file.write("\n")