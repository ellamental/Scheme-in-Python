(scheme-syntax define-primitive "
def f(expr):
  frame[expr.car] = Primitive(eval(expr.cdr.car))
")

(scheme-syntax define "
def f(expr):
  frame[expr.car] = scheme_eval(expr.cdr.car)
")

(scheme-syntax if "
def f(expr):
  if scheme_eval(expr.car):
    return scheme_eval(expr.cdr.car)
  else:
    return scheme_eval(expr.cdr.cdr.car)
")
