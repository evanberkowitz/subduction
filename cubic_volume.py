import sys
import numpy

import O_h
import D_4h
import D_2h
import D_3d

class boost:
    def __init__(self, vec=None):
        if vec==None:
            vec=[0,0,0]
        self.vector=vec
        self.parity=numpy.mod(vec, 2)

        # Sort to make the group selection easier.
        temp = [ abs(entry) for entry in self.vector]
        temp.sort()
        [x, y, z] = temp

        if x==y==z==0:
            self.group=O_h
        elif x==y==0 and z!=0:
            self.group=D_4h
        elif x==0 and y==z:
            self.group=D_2h
        elif x==y==z:
            self.group=D_3d
        elif x==y and x!=z:
            # // TODO: Fill in this group.
            self.group=None
        elif x!=y and y==z:
            # // TODO: Fill in this group.
            self.group=None
        elif x!=y and x!=z and y!=z:
            # // TODO: Fill in this group.
            self.group=None


    def n_squareds(self, up_to):
        n = int(numpy.ceil(numpy.sqrt(up_to)))+1
        return  list(set([ (x+0.5*self.parity[0])**2 + (y+0.5*self.parity[1])**2 + (z+0.5*self.parity[2])**2 for x in range(n) for y in range(n) for z in range(n) if (x+0.5*self.parity[0])**2 + (y+0.5*self.parity[1])**2 + (z+0.5*self.parity[2])**2 < up_to ]))
        

    def relative_momenta(self,ns):
        n = int(numpy.ceil(numpy.sqrt(ns)))+1
        return [ [x, y, z] + 0.5*self.parity for x in range(-n,n) for y in range(-n,n) for z in range(-n,n) if (x+0.5*self.parity[0])**2 + (y+0.5*self.parity[1])**2 + (z+0.5*self.parity[2])**2 == ns ]