from __future__ import print_function
import os, sys
import argparse
import numpy
import irreps
import octahedral
import n_squared

nsq = n_squared.vectors

print( octahedral.group )

# print("nsquared table")
# [ print(n,len(nsq(n)), [ len(octahedral.group.on(i)) for i in nsq(n) ] ,nsq(n)) for n in range(20) ]

# v=octahedral.group.on([0,0,1])
# print("Image of [0,0,1] under O_H:", v)
#
# c=octahedral.group.classes[1]
# print(c)
# print(nsq(3))
# print(octahedral.group.on(nsq(3)[0]))
# print(c.character_nsq(octahedral.group.on(nsq(3)[0])))
# print(octahedral.group.nsq_degeneracy("A1g",nsq(0)[0]))

# def test(ns, irrep):
#     return octahedral.group.nsq_degeneracy(irrep,nsq(ns)[0])
#
# [ print(n, test(n,"Eu")) for n in range(7) ]
# [ print(irrep, test(14,irrep)) for irrep in octahedral.group.irreps.keys() ]

print(octahedral.group.classes[1].ops[0])
print(octahedral.group.classes[1].ops[0].representation(octahedral.group.on(nsq(3)[0])))

P = octahedral.group.nsq_projector("Eg",nsq(1)[0])

print(P)
