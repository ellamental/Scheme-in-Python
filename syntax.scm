(scheme-syntax define-primitive "
def f(expr):
  set_symbol(expr.car, Primitive(eval(expr.cdr.car)), global_environment)
")

(scheme-syntax define "
def f(expr):
  set_symbol(expr.car, scheme_eval(expr.cdr.car), global_environment)
")

(scheme-syntax if "
def f(expr):
  if scheme_eval(expr.car):
    return scheme_eval(expr.cdr.car)
  else:
    return scheme_eval(expr.cdr.cdr.car)
")
