"""
scheme_read.py
(c)2011 Nick Zarczynski

For most code you should import this as: 
from scheme_read import scheme_read

This code assumes the file object being passed to scheme_read is of type
buffered_input, or at minimum provides f.getc/ungetc/peek/remove_whitespace.

This code is a pretty straight-forward port of the read function found in 
Bootstrap Scheme by Peter Michaux found at 
http://michaux.ca/articles/scheme-from-scratch-introduction
"""

def is_delimiter(c):
  """Is c a valid expression delimiter?"""
  return c in (' ', '(', ')', '\"', ';', '\n') or not c

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

def scheme_read(f):
  f.remove_whitespace()
  c = f.getc()
  if (c.isdigit() or (c == '-' and f.peek().isdigit() or f.peek() == '.')
      or (c == '.' and f.peek().isdigit())):
    f.ungetc(c)
    return read_number(f)
  else:
    return "scheme_read: not implemented"
