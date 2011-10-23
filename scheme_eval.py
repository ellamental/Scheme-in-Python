"""
scheme_eval.py
(c)2011 Nick Zarczynski

For most code you should import this as: 
from scheme_eval import scheme_eval
"""

from scheme_types import Symbol, Pair, Primitive
from buffered_input import Buff
from scheme_read import scheme_read

frame = {}
special_forms = {}

def lookup_symbol_value(symbol):
  try:
    return frame[symbol]
  except KeyError:
    return "Error: Unbound variable"

def self_evaluating(expr):
  t = type(expr)
  return t is int or t is float or t is str or t is bool

def scheme_eval(expr):
  if self_evaluating(expr):
    return expr
  elif type(expr) is Symbol:
    return lookup_symbol_value(expr)
  elif type(expr) is Pair:
    if expr.car in special_forms:
      return special_forms[expr.car](expr.cdr)
    else:
      return scheme_apply(scheme_eval(expr.car), [scheme_eval(a) for a in expr.cdr])
  else:
    return "scheme_eval: not implemented"

def scheme_apply(proc, args):
  if type(proc) is Primitive:
    return apply(proc.fn, args)
  else:
    return "Error: Undefined procedure"

def special_form_handler(expr):
  """Register a symbol with a Python function named "f" that implements a special form"""
  exec(expr.cdr.car)
  special_forms[expr.car] = f

def load(expr):
  """Given a filename, open it and eval each expression in the global_environment"""
  f = open(expr.car, 'r')
  b = Buff(f)
  while b.peek():
    scheme_eval(scheme_read(b))
    b.remove_whitespace()
  f.close()

special_forms['scheme-syntax'] = special_form_handler
special_forms['load'] = load
