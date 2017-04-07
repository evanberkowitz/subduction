import os, sys
import argparse
import numpy
import n_squared
import O_h
import D_4h
import D_2h
import block_diagonalize
import Center_of_Mass

boost = Center_of_Mass.Boost([1,1,1])
print(boost.vector)
print(boost.parity)

[ print(n, boost.relative_momenta(n)) for n in boost.n_squareds(10) ]
[ print(n, len(boost.relative_momenta(n))) for n in boost.n_squareds(10) ]

# exit()

def degeneracy_table(G, n):
    row_format = row_format = "{:>5}{:>12}{:>12} {:<30}" + "{:>5}" * len(G.irreps)
    print(row_format.format("n^2", "degeneracy", "vector", "solid", *(G.irreps.keys()) ))
    [ print(row_format.format(n, len(O_h.group.on(vec)), str(vec), n_squared.shape(vec), *[ (lambda d: "" if d==0 else d)(numpy.sum(numpy.array(G.nsq_degeneracy(irrep,vec).astype(int)))) for irrep in G.irreps.keys() ])) for n in range(n) if len(n_squared.vectors(n)) is not 0 for vec in n_squared.vectors(n) ]
    return None

nsq_max=24
for G in [O_h, D_4h, D_2h]:
    print( G.group )
    degeneracy_table(G.group, nsq_max)

mat=D_4h.group.nsq_projector("B1g", n_squared.vectors(5)[0])
print(mat)
perm = block_diagonalize.indices(mat)
print(perm)

[ print(mat[p,[p]]) for p in perm ]

exit()

mat=O_h.group.nsq_projector("Eg", n_squared.vectors(5)[0])
print(mat)
(evals, evecs) = numpy.linalg.eig(mat)
evals = numpy.around(evals, 14)
evecs = numpy.around(evecs, 14)
print(evals)
print(evecs)

mat=D_4h.group.nsq_projector("B1g", n_squared.vectors(5)[0])
print(mat)
(evals, evecs) = numpy.linalg.eig(mat)
evals = numpy.around(evals, 14)
evecs = numpy.around(evecs, 14)
print(evals)
print(evecs)

print(O_h.group.on(n_squared.vectors(5)[0]))

exit()

mat=O_h.group.nsq_projector("A1g", n_squared.vectors(1)[0])
print(mat)
(evals, evecs) = numpy.linalg.eig(mat)
evals = numpy.around(evals, 14)
evecs = numpy.around(evecs, 14)
print(evals)
print(evecs)

mat=D_4h.group.nsq_projector("A1g", n_squared.vectors(1)[0])
print(mat)
(evals, evecs) = numpy.linalg.eig(mat)
evals = numpy.around(evals, 14)
evecs = numpy.around(evecs, 14)
print(evals)
print(evecs)

mat=D_2h.group.nsq_projector("Ag", n_squared.vectors(1)[0])
print(mat)
(evals, evecs) = numpy.linalg.eig(mat)
evals = numpy.around(evals, 14)
evecs = numpy.around(evecs, 14)
print(evals)
print(evecs)

print(O_h.group.on(n_squared.vectors(1)[0]))

mat=D_4h.group.nsq_projector("Eg", n_squared.vectors(2)[0])
print(mat)
(evals, evecs) = numpy.linalg.eig(mat)
evals = numpy.around(evals, 14)
evecs = numpy.around(evecs, 14)
print(evals)
print(evecs)

print(O_h.group.on(n_squared.vectors(2)[0]))

# mat=D_4h.group.nsq_projector("B1g", n_squared.vectors(1)[0])
# print(mat)
# (evals, evecs) = numpy.linalg.eig(mat)
# evals = numpy.around(evals, 14)
# evecs = numpy.around(evecs, 14)
# print(evals)
# print(evecs)
#
# mat=D_2h.group.nsq_projector("Ag", n_squared.vectors(1)[0])
# print(mat)
# (evals, evecs) = numpy.linalg.eig(mat)
# evals = numpy.around(evals, 14)
# evecs = numpy.around(evecs, 14)
# print(evals)
# print(evecs)
