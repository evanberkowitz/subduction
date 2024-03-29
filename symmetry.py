from __future__ import print_function
import itertools
import numpy
import numpy.linalg

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
        
    def orbit(self, vec):
        return self.on(vec)
        
    def nsq_degeneracy(self, irrep, nsq_vec):
        # return { c.name:c.character_nsq(self.on(nsq_vec)) for c in self.classes }
        if not( irrep in self.irreps ):
            return 0;
        return numpy.sum([ len(c) * c.character(irrep) * c.character_nsq(self.on(nsq_vec)) for c in self.classes ]) / len(self)

    def nsq_projector(self, irrep, nsq_vec):
        if not( irrep in self.irreps ):
            return 0;
        orbit = self.on(nsq_vec)

        # // FIXME: this logic only works if the irreps are known---which isn't (currently) the case for the "little" and "relative" groups.
        dim_irrep = [ c.character(irrep) for c in self.classes if c.name is "E" ][0]
        return numpy.sum(numpy.array([ dim_irrep / len(self) * c.character(irrep) * R.representation(orbit) for c in self.classes for R in c.ops ]) , axis=0)

    def states(self, irrep, nsq_primitive):
        # // TODO: what am I doing?
        # // I think I want this function to be the "final" function that gives me lists of pair of vectors (states and weights).
        projector  = self.nsq_projector(irrep, nsq_primitive)
        eig_syss   = numpy.linalg.eig(projector)
        return eig_syss
        # evals      = numpy.around(eig_syss[:][0],PRECISION)
        # evecs      = numpy.around(eig_syss[:][1],PRECISION)
        # return [evals, evecs]
    
    def __str__(self):
        s=self.name+" --- "+str(len(self))+" operations:\n    "+"\n    ".join(map(str,self.classes))
        return s
        
    def __len__(self):
        return numpy.sum([len(c) for c in self.classes])
        
    def little(self, vec):
        if vec == [0,0,0]:
            G=self
        else:
            G = Group("Little group of "+self.name+" that leaves the vector "+str(vec)+" invariant.",
                [c for c in [ Class(c.name, [ op for op in c.ops if (op.on(vec) == numpy.array(vec)).all() ]) for c in self.classes ] if len(c) is not 0], 
                # // TODO: regroup the operations into appropriate classes, because classes may split.
                [ "Irreps?" ]
                )
        return G
        
    def relative(self, vec):
        if vec == [0, 0, 0]:
            G=self
        else:
            G = Group("Subgroup of "+self.name+" that leaves the axis parallel to "+str(vec)+" invariant.",
                [c for c in [ Class(c.name, [ op for op in c.ops if (op.on(vec) == numpy.array(vec)).all() or (op.on(vec) == -numpy.array(vec)).all() ]) for c in self.classes ] if len(c) is not 0], 
                [ "Irreps?" ]
                )
        return G
        
# // TODO: Write a function that can take a group and, based on its operations, identify it and thereby tell us which irreps there are, and the characters.
# // TODO: how to compute the character of an operation or symmetry class?  Ideally this would be a method associated with the appropriate python class.