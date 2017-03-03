#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This program DOES SOME STUFF.
"""

from server import Printer
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

    data = downloadData(url)
    result = saveData(data)
    parser = argparse.ArgumentParser()

    parser.add_argument('url', help='Enter the data url')
    args = parser.parse_args()

    if args.url:
        csvdata = download_data(args.url)
        process_data(csvdata)
    else:
        print 'error'
    pass

if __name__ == '__main__':
    main()
