#!/usr/bin/env python
# __author__: hexing
class FoundException(Exception):
    pass

try:
    v = 1/0
    raise FoundException("aaaaaaaaaaaa")
except ZeroDivisionError:
    raise FoundException("cccccc")
except FoundException:
    raise FoundException("aaaaa")