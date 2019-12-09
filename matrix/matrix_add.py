'''
Created on Dec. 6, 2019

@author: lauzo
'''


def add(*args):
    r = []
    rows = zip(*args)
    print(rows)
    for row in rows:
        add_vals = zip(*row)
        r.append([sum(val) for val in add_vals])
    return r