"""
buffered_input.py
(c)2011 Nick Zarczynski
License: BSD
version 0.1

Buff implements getc, ungetc and peek methods similar to those found in C.
"""

class Buff:
  def __init__(self, f):
    self.f = f
    self.last = []
  
  def getc(self):
    if self.last:
      return self.last.pop(0)
    else:
      return self.f.read(1)
  
  def ungetc(self, c):
    self.last.insert(0, c)
  
  def peek(self):
    if self.last:
      return self.last[0]
    else:
      c = self.f.read(1)
      self.last.append(c)
      return c
  
  def remove_whitespace(self):
    c = self.getc()
    while c:
      if c == ' ':
        c = self.getc()
      elif c == '\n':
        c = self.getc()
      elif c == ';':
        c = self.getc()
        while c and c != '\n':
          c = self.getc()
        self.ungetc(c)  
      else:
        self.ungetc(c)
        break
