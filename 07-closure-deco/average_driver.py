from average import make_averager

avg = make_averager()
print(avg(10))
print(avg(11))
print(avg(12))
print(avg.__code__.co_varnames)
print(avg.__code__.co_freevars)
print(avg.__closure__)  # doctest: +ELLIPSIS
print(avg.__closure__[0].cell_contents)
