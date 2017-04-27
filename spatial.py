import numpy

import O_h
import D_4h
import D_2h
import D_3d

class boost:
    def __init__(self, group, vec=None):
        if vec==None:
            vec=[0,0,0]
        self.vector=vec
        self.parity=numpy.mod(vec,2)
        
        self.group=group.relative(vec)
    
    def n_squareds(self, up_to, nsq_min=0):
        n = int(numpy.ceil(numpy.sqrt(up_to)))+1
        return  list(set([ (x+0.5*self.parity[0])**2 + (y+0.5*self.parity[1])**2 + (z+0.5*self.parity[2])**2 for x in range(n) for y in range(n) for z in range(n) if nsq_min < (x+0.5*self.parity[0])**2 + (y+0.5*self.parity[1])**2 + (z+0.5*self.parity[2])**2 < up_to ]))
    
    def relative_momenta(self, ns):
        n = int(numpy.ceil(numpy.sqrt(ns)))+2
        # Generate a list of every vector with the right ns.
        every = [ [x, y, z] + 0.5*self.parity for x in range(-n,n) for y in range(-n,n) for z in range(-n,n) if (x+0.5*self.parity[0])**2 + (y+0.5*self.parity[1])**2 + (z+0.5*self.parity[2])**2 == ns ]
        
        # Now, whittle them down to just the "starters"---the ones that:
        #       don't transform into one another under the group action
        #       taken together, generate the set of every vector
        starters = [ ]
        while( len(every) > 0 ):
            new = every[0]
            starters += [ list(new) ]
            image = self.group.on(new)
            every = [ list(vec) for vec in every if list(vec) not in image ]      # Prune the image of the new starter.
        return starters

class volume:
    def __init__(self, vec=None):
        if vec==None:
            vec=[0,0,0]
        self.principal_axis=vec
        
        [x,y,z] = vec
        
        if x==y==z:
            self.group=O_h.group
            self.principal_axis=[0,0,1]
        elif x==y:
            self.principal_axis=[0,0,1]
            self.group=O_h.group.relative(self.principal_axis)
        elif y==z:
            self.principal_axis=[1,0,0]
            self.group=O_h.group.relative(self.principal_axis)
        elif z==x:
            self.principal_axis=[0,1,0]
            self.group=O_h.group.relative(self.principal_axis)
        elif x!=y and y!=z and z!=x:
            # // TODO: what is a sensible principal axis?
            self.group=D_2h.group
    
    def boost(self, vec=None):
        return boost(self.group, vec)

