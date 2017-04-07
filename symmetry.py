from __future__ import print_function
import itertools
import numpy
import numpy.linalg
import n_squared
import O_h

PRECISION=14 # numpy craps out at 16

def precision(lst):
    return numpy.around(lst, PRECISION)

def union(lst):
    plain = [ [ x for x in sub ] for sub in lst ]
    plain.sort()
    return list( vec for vec,_ in itertools.groupby(plain))    

class Operation:
    def on(self, vec):
        return vec
    
    def representation(self, nsq_vecs):
        return numpy.array([ [ (numpy.array(self.on(i)) == numpy.array(j)).all() for j in nsq_vecs ] for i in nsq_vecs]).astype(int)
    
    def __init__(self):
        pass
    
    def __str__(self):
        return "Default identity symmetry operation."
        
    def __mul__(self, other):
        return Composition(self,other)

identity=Operation()

class Composition(Operation):
    
    def __init__(self, left, right):
        self.left  = left
        self.right = right

    def on(self, vec):
        return self.left.on(self.right.on(vec))
    
    def __str__(self):
        return str(self.left) + " following " + str(self.right)

class Rotation(Operation):
    def __init__(self, vec=None, theta=None):
        Operation.__init__(self)
        if vec is None:
            mat=[ 0,0,1 ]
        if theta is None:
            theta=0
        
        [x,y,z]=vec
        
        # Normalize:
        [x,y,z]=[ direction/numpy.sqrt(x*x+y*y+z*z) for direction in [x,y,z] ]
        c=numpy.cos(theta)
        s=numpy.sin(theta)
    
        # 3D rotation matrix in full generality.
        self.vec = vec
        self.theta = theta
        self.rep = [
            [ c + x*x*(1-c), x*y*(1-c)-z*s, x*z*(1-c)+y*s  ],
            [ y*x*(1-c)+z*s, c + y*y*(1-c), y*z*(1-c)-x*s  ],
            [ z*x*(1-c)-y*s, z*y*(1-c)+x*s, c + z*z*(1-c)  ]
        ]
    
    def on(self, vec):
        return precision(numpy.dot(self.rep, vec))
    
    def __str__(self):
        return "rotation around "+str(self.vec)+" by "+str(self.theta*360/(2*numpy.pi))+" degrees"
        

class Reflection(Operation):
    def __init__(self, mask):
        self.axes=mask
        
    def on(self, vec):
        return [ precision(sign*component) for sign,component in zip(self.axes,vec) ]
    
    def __str__(self):
        return "reflection given by "+str(self.axes)

inversion = Reflection([-1,-1,-1])

class Class:
    def __init__(self, name=None, ops=None, characters=None, desc=None):
        if ops is None:
            name="E"
            ops=[ Operation() ]
        self.ops=ops
        self.name=name
        self.long_description=desc
        self.characters=characters
    
    def on(self, vec):
        return union([ precision(op.on(vec)) for op in self.ops ])
        
    def character(self, irrep):
        return self.characters[irrep]
        
    def character_nsq(self, nsq_vecs):
        candidates = [ numpy.sum([ 1 for vec in nsq_vecs if (op.on(vec) == precision(numpy.array(vec))).all() ]) for op in self.ops ]
        if (candidates == candidates[0]).all():
            return candidates[0]
        else:
            print("Uh-oh")
            return 0
    
    
    def __len__(self):
        return len(self.ops)
    
    def __str__(self):
        if len(self.ops) == 1:
            return "Symmetry class "+self.name+", with "+str(len(self.ops))+" operation."
        return "Symmetry class "+self.name+", with "+str(len(self.ops))+" operations."
        
class Group:
    def __init__(self, name=None, classes=None, irreps=None):
        if name is None or classes is None:
            name="Identity"
            classes=[]
        self.name=name
        self.classes=classes
        self.irreps=irreps
    
    def on(self, vec):
        return union([ op.on(vec) for c in self.classes for op in c.ops ])
        
    def nsq_degeneracy(self, irrep, nsq_vec):
        # return { c.name:c.character_nsq(self.on(nsq_vec)) for c in self.classes }
        if not( irrep in self.irreps ):
            return 0;
        return numpy.sum([ len(c) * c.character(irrep) * c.character_nsq(O_h.group.on(nsq_vec)) for c in self.classes ]) / len(self)

    def nsq_projector(self, irrep, nsq_vec):
        if not( irrep in self.irreps ):
            return 0;
        image = O_h.group.on(nsq_vec)
        return numpy.sum(numpy.array([ 1.0 / len(self) * c.character(irrep) * R.representation(image) for c in self.classes for R in c.ops ]) , axis=0)

    def nsq_states(self, irrep, nsq):
        primitives = n_squared.vectors(nsq)
        images     = [ O_h.group.on(p) for p in primitives ]
        projectors = [ self.nsq_projector(irrep, i) for i in primitives ]
        eig_syss   = [ numpy.linalg.eig(p) for p in projectors ]
        return eig_syss
        # evals      = numpy.around(eig_syss[:][0],PRECISION)
        # evecs      = numpy.around(eig_syss[:][1],PRECISION)
        # return [evals, evecs]
    
    def __str__(self):
        s=self.name+" --- "+str(len(self))+" operations:\n    "+"\n    ".join(map(str,self.classes))
        return s
        
    def __len__(self):
        return numpy.sum([len(c) for c in self.classes])
        
