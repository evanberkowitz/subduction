from __future__ import print_function
import os, sys
import argparse
import numpy
import octahedral
import n_squared

print( octahedral.group )

print("Degeneracy table")

irreps=["A1g", "A2g", "T1g", "T2g", "Eg", "A1u", "A2u", "T1u", "T2u", "Eu"]
row_format = "{:>5}{:>12}{:>12}" + "{:>5}" * len(irreps)
print(row_format.format("n^2", "degeneracy", "vector", *irreps))
[ print(row_format.format(n, len(octahedral.group.on(vec)), str(vec), *[ (lambda d: "" if d==0 else d)(numpy.sum(numpy.array(octahedral.group.nsq_degeneracy(irrep,vec).astype(int)))) for irrep in irreps ])) for n in range(24) if len(n_squared.vectors(n)) is not 0 for vec in n_squared.vectors(n) ]


# print(octahedral.group.classes[1].ops[0])
# print(octahedral.group.classes[1].ops[0].representation(octahedral.group.on(nsq(3)[0])))
#
# P = octahedral.group.nsq_projector("T2g",nsq(14)[0])
#
# print(P)
#
# eig_vals=numpy.around(numpy.linalg.eig(P)[0], 10)
# eig_vals.sort()
#
# print(eig_vals)

# es=octahedral.group.nsq_states("T2g", 9)
#
# # print( es )
# print( numpy.around(numpy.array(es[1][0]), 14) )