import os, sys
import argparse
import numpy
import n_squared
import O_h
import D_4h
import D_2h
import block_diagonalize
import cubic_volume

def degeneracy_table(G, n):
    row_format = "{:>5}{:>12}{:>20} {:<25}" + "{:>5}" * len(G.irreps)
    print(row_format.format("n^2", "degeneracy", "vector", "solid", *(G.irreps) ))
    [ print(row_format.format(n, len(O_h.group.on(vec)), str(vec), n_squared.shape(vec), *[ (lambda d: "" if d==0 else d)(numpy.sum(numpy.array(G.nsq_degeneracy(irrep,vec).astype(int)))) for irrep in G.irreps ])) for n in range(n) if len(n_squared.vectors(n)) is not 0 for vec in n_squared.vectors(n) ]
    return None

# Reproduce Luu & Savage:
nsq_max=24
for G in [O_h]: #, D_4h, D_2h]: # // NOTE: I'm not sure the degeneracy table works for D_4h and D_2h (but I think it does).
    print( G.group )
    degeneracy_table(G.group, nsq_max)

print("\n\n\n\n")
nsq_max=12
boost = cubic_volume.boost([1,1,1])
print("Now consider a cubic volume boosted by ",boost.vector)
print("The parity of the boost is ",boost.parity)

print("The boost breaks the O_H symmetry.  We are left with the")
print(boost.group)

print("Even though there are many vectors for a given n^2 that would go into one another if we could act with the full O_H")
print("the loss of some generators partitions the set of those vectors into smaller sets that transform into one another under the group action.")
row_format = "{:>5}{:>12}{:>20}"
print(row_format.format("n^2", "degeneracy", "vector"))
[ print(row_format.format(n, len( boost.group.on(v) ), str(v) )) for n in boost.n_squareds(nsq_max) for v in boost.relative_momenta(n)]

print("\n\n\n\n")
nsq_max=7
boost = cubic_volume.boost([1,1,3])
print("Now consider a cubic volume boosted by ",boost.vector," instead.  This obviously has less symmetry than the previous boost.")
print("The parity of the boost is ",boost.parity)
print("Since the parity is the same, the n^2 values are the same as the [1,1,1] boost.")

print("The boost breaks the O_H symmetry.  We are left with the")
print(boost.group)

print("Even though the n^2 values are the same,")
print("different generators survive, so the sets that transform into one another under the group action are different.")
row_format = "{:>5}{:>12}{:>20}"
print(row_format.format("n^2", "degeneracy", "vector"))
[ print(row_format.format(n, len( boost.group.on(v) ), str(v) )) for n in boost.n_squareds(nsq_max) for v in boost.relative_momenta(n)]

print("\n\n\n\n")
nsq_max=7
boost = cubic_volume.boost([1,1,2])
print("Now consider a cubic volume boosted by ",boost.vector," instead.")
print("The parity of the boost is ",boost.parity)
print("Since the parity is different, the n^2 values are different.")

print("The boost breaks the O_H symmetry.  We are left with the")
print(boost.group)

print("Again, different generators survive, so the sets that transform into one another under the group action are different.")
row_format = "{:>5}{:>12}{:>20}"
print(row_format.format("n^2", "degeneracy", "vector"))
[ print(row_format.format(n, len( boost.group.on(v) ), str(v) )) for n in boost.n_squareds(nsq_max) for v in boost.relative_momenta(n)]

print("\n\n\n\n")
nsq_max=7
boost = cubic_volume.boost([2,2,2])
print("Now consider a cubic volume boosted by ",boost.vector,".")
print("The parity of the boost is ",boost.parity)
print("Since the parity matches that of [0,0,0], the n^2 values will be the same---integers.")

print("The boost breaks the O_H symmetry.  We are left with the")
print(boost.group)

print("Again, because different generators survive, so for a given n^2 we get multiple sets that are joined in the unboosted case.")
row_format = "{:>5}{:>12}{:>20}"
print(row_format.format("n^2", "degeneracy", "vector"))
[ print(row_format.format(n, len( boost.group.on(v) ), str(v) )) for n in boost.n_squareds(nsq_max) for v in boost.relative_momenta(n)]





print("\n\n\n\n")
print("We can look at a particularly tricky case---when there's more than one copy of an irrep for a given n^2")
print("For example, consider the Eg representation of O_H with n^2=5.")
print("The projector to that irrep, on the basis of the n^2=5 vectors is")
mat=O_h.group.nsq_projector("Eg", n_squared.vectors(5)[0])
print(mat)
(evals, evecs) = numpy.linalg.eig(mat)
print("The eigenvalues of that matrix are")
evals = numpy.around(evals, 14)
evecs = numpy.around(evecs, 14)
print(evals)
print("so you see that mostly they're 0, but 4 are 1.  That jibes with the claim that it's 2 Eg irreps, since |Eg|=2.")
print("without further logic we can't say how to get the 'L_z' analog.")
# print(evecs)

print("// TODO: The ultimate goal is to be able to specify a spatial volume, a center of mass boost, and an nsquared and get, for each allowed irrep, a list of states made out of vectors and corresponding weights.")
