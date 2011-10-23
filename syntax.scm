(scheme-syntax define-primitive "
def f(expr, env):
  set_symbol(expr.car, Primitive(eval(expr.cdr.car)), env)
")

(scheme-syntax define "
def f(expr, env):
  set_symbol(expr.car, scheme_eval(expr.cdr.car, env), env)
")

(scheme-syntax if "
def f(expr, env):
  if scheme_eval(expr.car, env):
    return scheme_eval(expr.cdr.car, env)
  else:
    return scheme_eval(expr.cdr.cdr.car, env)
")
