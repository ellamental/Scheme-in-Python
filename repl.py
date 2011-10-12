#!/usr/bin/env python
"""
repl.py
(c)2011 Nick Zarczynski
License: BSD

A simple repl
"""

import sys
from scheme_read import scheme_read
from scheme_eval import scheme_eval
from buffered_input import Buff

while True:
  print "> ", 
  print scheme_eval(scheme_read(Buff(sys.stdin)))
