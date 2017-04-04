import itertools
import numpy

PRECISION=14 # numpy craps out at 16

def precision(lst):
    return numpy.around(lst, PRECISION)

def union(lst):
    plain = [ [ x for x in sub ] for sub in lst ]
    plain.sort()
    # return numpy.unique(precision(lst))
    return list( vec for vec,_ in itertools.groupby(plain))    

class Operation:
    def on(self, vec):
        return vec
    
    def __init__(self):
        pass
    
    def __str__(self):
        return "Default identity symmetry operation."
        
    def __mul__(self, other):
        return Composition(self,other)

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
        return numpy.array([ precision(sign*component) for sign,component in zip(self.axes,vec) ])
    
    def __str__(self):
        return "reflection given by "+str(self.axes)


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
        return union([ precision(numpy.dot(op, vec)) for op in self.ops ])
        
    def character(irrep):
        return self.characters[irrep]
        
    def __len__(self):
        return len(self.ops)
    
    def __str__(self):
        return "Symmetry class "+self.name+", with "+str(len(self.ops))+" operations."
        
class Group:
    def __init__(self, name=None, classes=None):
        if name is None or classes is None:
            name="Identity"
            classes=[]
        self.name=name
        self.classes=classes
    
    def on(self, vec):
        return union([ op.on(vec) for c in self.classes for op in c.ops ])
    
    def __str__(self):
        s=self.name+" --- "+str(len(self))+" operations:\n    "+"\n    ".join(map(str,self.classes))
        return s
        
    def __len__(self):
        return reduce(numpy.add, map(len, self.classes))