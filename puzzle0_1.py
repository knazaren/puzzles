from puzzle_lib import *
if __name__ == "__main__":
    d = build_dict(poem)
    #print d
    dr = {}
    for k in d:
        v = d[k]
        dr[v] = k
    say_something(dr, [56, 38, 44, 56, 29])


