#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is a constructor for the Request class."""


class Request:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def get_stamp(self):
        return self.timestamp

    def get_pages(self):
        return self.pages

    def wait_time(self, current_time):
        return current_time - self.timestamp