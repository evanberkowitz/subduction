from __future__ import print_function
import os, sys
import argparse
import numpy
import n_squared
import O_h
import D_4h

print( O_h.group )

print("Degeneracy table")

irreps=["A1g", "A2g", "T1g", "T2g", "Eg", "A1u", "A2u", "T1u", "T2u", "Eu"]
row_format = "{:>5}{:>12}{:>12} {:<30}" + "{:>5}" * len(irreps)
print(row_format.format("n^2", "degeneracy", "vector", "solid", *irreps))
[ print(row_format.format(n, len(O_h.group.on(vec)), str(vec), n_squared.shape(vec), *[ (lambda d: "" if d==0 else d)(numpy.sum(numpy.array(O_h.group.nsq_degeneracy(irrep,vec).astype(int)))) for irrep in irreps ])) for n in range(6) if len(n_squared.vectors(n)) is not 0 for vec in n_squared.vectors(n) ]


# print(O_h.group.classes[1].ops[0])
# print(O_h.group.classes[1].ops[0].representation(O_h.group.on(nsq(3)[0])))
#
# P = O_h.group.nsq_projector("T2g",nsq(14)[0])
#
# print(P)
#
# eig_vals=numpy.around(numpy.linalg.eig(P)[0], 10)
# eig_vals.sort()
#
# print(eig_vals)

# es=O_h.group.nsq_states("T2g", 9)
#
# # print( es )
# print( numpy.around(numpy.array(es[1][0]), 14) )

print( D_4h.group )
row_format = "{:>5}{:>12}{:>12} {:<30}" + "{:>5}" * len(D_4h.group.irreps)
print(row_format.format("n^2", "degeneracy", "vector", "solid", *(D_4h.group.irreps.keys()) ))
[ print(row_format.format(n, len(O_h.group.on(vec)), str(vec), n_squared.shape(vec), *[ (lambda d: "" if d==0 else d)(numpy.sum(numpy.array(D_4h.group.nsq_degeneracy(irrep,vec).astype(int)))) for irrep in D_4h.group.irreps.keys() ])) for n in range(24) if len(n_squared.vectors(n)) is not 0 for vec in n_squared.vectors(n) ]