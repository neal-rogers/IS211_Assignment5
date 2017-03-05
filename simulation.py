#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This program DOES SOME STUFF.
"""


import csv
import time


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class Request:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def get_stamp(self):
        return self.timestamp

    def wait_time(self, current_time):
        return current_time - self.timestamp

class Server:
    def __init__(self, ):
        self.page_rate = ppm
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        if self.current_task != None:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        if self.current_task != None:
            return True
        else:
            return False

    def start_next(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60 / self.page_rate


# This function needs to accept the input_file
def simulateOneServer(num_seconds, ):
    lab_printer = Server()
    print_queue = Queue()
    waiting_times = []

    for current_second in range(num_seconds):

        if new_print_task():
            task = Task(current_second)
            print_queue.enqueue(task)

        if (not lab_printer.busy()) and (not print_queue.is_empty()):
            new.task - print_queue.dequeue()
            waiting_times.append(next_task.wait_time(current_second))
            lab_printer.startNext(next_task)

        lab_printer.tick()

        average_wait = sum(waiting_times) / len(waiting_times)
        print("Average Wait %6.2f secs %3d tasks remaining." % (average_wait, print_queue.size()))

def simulateManyServers():
    pass


def main():
    simulateOneServer(input_file)



if __name__ == '__main__':
    main()
