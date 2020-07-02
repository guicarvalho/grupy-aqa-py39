"""
d1  = {"a": 1}
d2 = {"b": 2}

d = dict(d1, **d2)
print(d)

d = d1.copy()
d.update(d2)
print(d)

d = {**d1, **d2}
print(d)
"""

d1  = {"a": 1}
d2 = {"b": 2}

d = d1 | d2
print(d)

d1 |= d2
print(d1)
