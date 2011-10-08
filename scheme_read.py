"""
scheme_read.py
(c)2011 Nick Zarczynski
License: BSD

For most code you should import this as: 
from scheme_read import scheme_read

This code assumes the file object being passed to scheme_read is of type
buffered_input, or at minimum provides f.getc/ungetc/peek/remove_whitespace.

This code is a pretty straight-forward port of the read function found in 
Bootstrap Scheme by Peter Michaux found at 
http://michaux.ca/articles/scheme-from-scratch-introduction
"""

from scheme_types import Symbol, the_empty_list, Pair

def is_delimiter(c):
  """Is c a valid expression delimiter?"""
  return c in (' ', '(', ')', '\"', ';', '\n') or not c

def is_initial(c):
  """Is c a valid initial character for an identifier?"""
  return c.isalpha() or c in '-+*/><=?!&'

def read_number(f):
  buf = []
  c = f.getc()
  while not is_delimiter(c):
    buf.append(c)
    c = f.getc()
  f.ungetc(c)
  buf = "".join(buf)
  if '.' in buf:
    return float(buf)
  elif '/' in buf:
    return "rationals not implemented"
  else:
    return int(buf)

def read_expected_string(f, s):
  """Consume expected characters from the input buffer."""
  expected_chars = list(s)
  c = f.getc()
  while expected_chars:
    if c == expected_chars[0]:
      expected_chars.pop(0)
      c = f.getc()
    else:
      return "unexpected character"

def read_character(f):
  c = f.getc()
  if c == 's' and f.peek() == 'p':
    read_expected_string(f, "pace")
    return ' '
  elif c == 'n' and f.peek() == 'e':
    read_expected_string(f, "ewline")
    return '\n'
  else:
    return c

def read_symbol(f):
  buf = []
  c = f.getc()
  while not is_delimiter(c):
    buf.append(c)
    c = f.getc()
  f.ungetc(c)
  return ''.join(buf)

def read_string(f):
  buf = []
  c = f.getc()
  while c != '\"':
    buf.append(c)
    c = f.getc()
  return ''.join(buf)

def read_pair(f):
  f.remove_whitespace()
  c = f.getc()
  if c == ')':
    return the_empty_list
  f.ungetc(c)
  car = scheme_read(f)
  f.remove_whitespace()
  cdr = read_pair(f)
  return Pair(car, cdr)

def scheme_read(f):
  f.remove_whitespace()
  c = f.getc()
  if (c.isdigit() or (c == '-' and f.peek().isdigit() or f.peek() == '.')
      or (c == '.' and f.peek().isdigit())):
    f.ungetc(c)
    return read_number(f)
  elif c == '#':
    c = f.getc()
    if c == 't':
      return True
    elif c == 'f':
      return False
    elif c == '\\':
      return read_character(f)
    else:
      return "Error boolean value must be #t or #f not #" + c
  elif is_initial(c):
    f.ungetc(c)
    return Symbol(read_symbol(f))
  elif c == '\"':
    return read_string(f)
  elif c == '(':
    return read_pair(f)
  else:
    return "scheme_read: not implemented"
