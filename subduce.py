from __future__ import print_function
import os, sys
import argparse
import irreps

def test(vec):
    print(vec, irreps.vec_to_angles(vec))

test([0,0,1])
test([0,0,-1])
test([0,1,0])
test([0,-1,0])
test([1,0,0])
test([-1,0,0])
test([0,1,1])

Y00=irreps.Ylm(0,0)
print(Y00([1,0,0]))

[ print(n,len(irreps.nsq(n)),irreps.nsq(n)) for n in range(20) ]


print(irreps.symmetry_image([0,0,1]))