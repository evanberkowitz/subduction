from __future__ import print_function
import os, sys
import argparse
import numpy
import n_squared
import O_h
import D_4h
import D_2h

def degeneracy_table(G, n):
    row_format = row_format = "{:>5}{:>12}{:>12} {:<30}" + "{:>5}" * len(G.irreps)
    print(row_format.format("n^2", "degeneracy", "vector", "solid", *(G.irreps.keys()) ))
    [ print(row_format.format(n, len(O_h.group.on(vec)), str(vec), n_squared.shape(vec), *[ (lambda d: "" if d==0 else d)(numpy.sum(numpy.array(G.nsq_degeneracy(irrep,vec).astype(int)))) for irrep in G.irreps.keys() ])) for n in range(n) if len(n_squared.vectors(n)) is not 0 for vec in n_squared.vectors(n) ]
    return None

for G in [O_h, D_4h, D_2h]:
    print( G.group )
    degeneracy_table(G.group, 24)


# # print(O_h.group.classes[1].ops[0])
# # print(O_h.group.classes[1].ops[0].representation(O_h.group.on(nsq(3)[0])))
# #
# # P = O_h.group.nsq_projector("T2g",nsq(14)[0])
# #
# # print(P)
# #
# # eig_vals=numpy.around(numpy.linalg.eig(P)[0], 10)
# # eig_vals.sort()
# #
# # print(eig_vals)
#
# # es=O_h.group.nsq_states("T2g", 9)
# #
# # # print( es )
# # print( numpy.around(numpy.array(es[1][0]), 14) )
#
