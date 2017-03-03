#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This program DOES SOME STUFF.
"""

from printer import Printer
from server import Server


def downloadData(url):
    response = urllib2.urlopen(url)
    data = response.read()
    return data


def simulateOneServer(input_file):
    pass


def simulateManyServers():
    return avg_latency


def main():
    simulateOneServer(input_file)
    pass

if __name__ == '__main__':
    main()
