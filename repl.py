"""
repl.py
(c)2011 Nick Zarczynski

A simple repl
"""

import sys
from scheme_read import scheme_read
from buffered_input import Buff

while True:
  print "> ", 
  print scheme_read(Buff(sys.stdin))
