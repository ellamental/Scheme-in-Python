"""
scheme_eval.py
(c)2011 Nick Zarczynski

For most code you should import this as: 
from scheme_eval import scheme_eval
"""

from scheme_types import Symbol, Pair, Primitive, the_empty_list
from buffered_input import Buff
from scheme_read import scheme_read

def current_environment(env):
  """Return the frame of the current environment"""
  return env.car

def enclosing_environment(env):
  """Return the environment stack with the first frame removed"""
  return env.cdr

def extend_environment(bindings, base_environment):
  """Push a new frame onto the given base_environment"""
  return Pair(bindings, base_environment)

global_environment = extend_environment({}, the_empty_list)
special_forms = {}

def set_symbol(symbol, val, env):
  """Set the binding (symbol, val) in the current frame of env"""
  current_environment(env)[symbol] = val

def lookup_symbol_value(symbol, environment):
  """Return the value of symbol or Unbound Symbol error"""
  env = environment
  while env != the_empty_list:
    if symbol in current_environment(env):
      return current_environment(env)[symbol]
    else:
      env = enclosing_environment(env)
  return "Error: Unbound symbol: " + symbol

def self_evaluating(expr):
  t = type(expr)
  return t is int or t is float or t is str or t is bool

def scheme_eval(expr):
  if self_evaluating(expr):
    return expr
  elif type(expr) is Symbol:
    return lookup_symbol_value(expr, global_environment)
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
