This is a simple Scheme interpreter written in Python.  There is also a [blog series detailing the development of this interpreter](http://nickzarr.com/blog4/series/scheme-in-python/).

The Scheme in Python project is a port of the [Scheme in Scheme](http://nickzarr.com/blog4/series/lispy-in-scheme/) project.  The goal is to implement a small subset of Scheme as an interpreter written in Python.

There are a number of goals for this project.  First, implementing Scheme in Scheme allowed us to "cheat" a bit by having access to the Scheme reader and data structures.  Using Python as the implementation language will force us to code the reader by hand and create new data structures where there isn't a one-to-one mapping from Scheme to Python.

There are also two auxiliary goals to this project.  Using Python should make this more accessible to programmers who are interested in language development, but are unfamiliar with Scheme.  Also I'm using this project as a way to familiarize myself with branching and merging in git, so each post will correspond to a branch in the repository.

All the code for this project will be hosted on GitHub.  The code is licensed under a BSD license if you are interested in forking it for any reason.  

This series will focus on building a very simple interpreter for the purpose of learning the steps involved in building one.  For this reason there will be no/very little error checking or optimization.  This port will be slightly more complicated than Scheme in Scheme so if you are interested in an even simpler interpreter look [here](http://nickzarr.com/blog4/series/lispy-in-scheme/).

With that out of the way, here's an example session:

    /code/Scheme in Python$ python scheme.py
    > 42
    42
    > -.42
    -0.42
    > 4/2
    rationals not implemented
    > #t
    True
    > #f
    False
    > #\a
    a
    > #\space
    
    > hello
    Error: Unbound symbol: hello
    > (define hello "world")

    > hello
    world
    > (if #t 1 0)
    1
    > (if #f 1 0)
    0
    > (+ 3 4)
    7
    > ((fn (x) x) 42)
    42
    > (define echo (fn (x) x))

    > (echo 42)
    42
    > (define add (fn (x y) (+ x y)))

    > (add 3 4)
    7



(c)2011 Nick Zarczynski

License: BSD
