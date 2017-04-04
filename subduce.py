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
[ print(row_format.format(n, len(octahedral.group.on(vec)), vec, *[ (lambda d: "" if d==0 else d)(numpy.sum(numpy.array(octahedral.group.nsq_degeneracy(irrep,vec).astype(int)))) for irrep in irreps ])) for n in range(24) if len(n_squared.vectors(n)) is not 0 for vec in n_squared.vectors(n) ]


