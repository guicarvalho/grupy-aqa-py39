"""
with open("f1", "w") as foo, open(
    "f2", "w"
) as baz, open("f3", "w") as bar:
    pass
"""

with (
    open("f1", "w") as foo,
    open("f2", "w") as baz,
    open("f3", "w") as bar
):
    pass
