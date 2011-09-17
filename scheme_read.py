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

def scheme_read(f):
  f.remove_whitespace()
  c = f.getc()
  if c.isdigit():
    return "Representation of a Scheme number."
  else:
    return "scheme_read: not implemented"

