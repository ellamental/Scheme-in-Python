#!/usr/bin/env python
"""
repl.py
(c)2011 Nick Zarczynski
License: BSD

A simple repl
"""

import sys
from scheme_read import scheme_read
from scheme_eval import scheme_eval, special_forms, global_environment
from scheme_types import Pair
from buffered_input import Buff

special_forms['load'](Pair("syntax.scm", None))

while True:
  inp = scheme_eval(scheme_read(Buff(sys.stdin)), global_environment)
  if inp != None:
    print ';===>', inp

