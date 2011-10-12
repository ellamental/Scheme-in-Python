"""
scheme_eval.py
(c)2011 Nick Zarczynski

For most code you should import this as: 
from scheme_eval import scheme_eval
"""

def scheme_eval(expr):
  if type(expr) is int:
    return expr
  else:
    return "scheme_eval: not implemented"