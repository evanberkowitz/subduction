import os, sys
import argparse
import numpy
import O_h
import D_4h
import D_2h
import block_diagonalize
import spatial

cube=spatial.volume([16,16,16])

# Here's a now-correct degeneracy table.
# // TODO: simplify degeneracy_table
# It would be better if rather than having to pass the group and the boost separately, one could just pass the boost.
# What stands in the way is that currently arbitrary volumes and boosts use the Group.relative procedure to construct subgroups, and this doesn't have logic to deduce what the available irreps and symmetry classes are and what the character tables should be.  Those are needed to automatically determine the group.
def degeneracy_table(G, boost, n):
    row_format = "{:>5}{:>12}{:>20} " + "{:>5}" * len(G.irreps)
    print(row_format.format("n^2", "degeneracy", "vector", *(G.irreps) ))
    [ print(row_format.format(n, len(G.on(vec)), str(vec), *[ (lambda d: "" if d==0 else d)(numpy.sum(numpy.array(G.nsq_degeneracy(irrep,vec).astype(int)))) for irrep in G.irreps ])) for n in range(n) if len(boost.relative_momenta(n)) is not 0 for vec in boost.relative_momenta(n) ]
    return None

# Reproduce Luu & Savage
print( O_h.group )
degeneracy_table(O_h.group,  cube.boost([0,0,0]), 24)

# Complete D_4h table
print( D_4h.group )
#  One can start with an anisotropic volume...
degeneracy_table(D_4h.group, spatial.volume([16,16,32]).boost([0,0,0]), 24)
# or, instead, one might take a cubic volume and do a parity-even boost along the z-axis
# The z-axis is special because the D_4h module assumes the z axis is the principal axis.
# degeneracy_table(D_4h.group, cube.boost([0,0,2]), 24) # This gives the same degeneracy table!

print( D_2h.group )
# I think there may be a bug, because these two:
degeneracy_table(D_2h.group, spatial.volume([16,32,48]).boost([0,0,0]), 24)
# degeneracy_table(D_2h.group, cube.boost([0,2,2]), 24)
# produce different degeneracy tables, sort of.  The former produces, for nsq=2,
    # 5           4   [-2.0, -1.0, 0.0]     1    1                        1    1
    # 5           4   [-2.0, 0.0, -1.0]     1         1              1         1
    # 5           4   [-1.0, -2.0, 0.0]     1    1                        1    1
    # 5           4   [-1.0, 0.0, -2.0]     1         1              1         1
    # 5           4   [0.0, -2.0, -1.0]     1              1         1    1
    # 5           4   [0.0, -1.0, -2.0]     1              1         1    1
# while the latter produces
    # 5           4   [-2.0, -1.0, 0.0]     1    1                        1    1
    # 5           4   [-1.0, -2.0, 0.0]     1    1                        1    1
    # 5           4   [0.0, -2.0, -1.0]     1              1         1    1
    # 5           4    [0.0, -2.0, 1.0]     1              1         1    1
# I think the first is correct, because O_h n^2 = 5 has degeneracy 24 = 6 * 4 = (first result)
# Somehow we're missing the vectors with 0 in the y entry.
# // FIXME: Sort out this mysterious D_2h mismatch.

# print("\n\n\n... and exit early.")
# exit()

print("\n\n\n\n")
cube=spatial.volume([16,16,16])
nsq_max=12
boost = cube.boost([1,1,1])
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
boost = cube.boost([1,1,3])
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
boost = cube.boost([1,1,2])
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
boost = cube.boost([2,2,2])
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
mat=O_h.group.nsq_projector("Eg", cube.boost([0,0,0]).relative_momenta(5)[0])
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
