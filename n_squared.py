import sys
import numpy

def vectors(ns):
    # Returns a list of all the vectors with nondecreasing, nonnegative integer entries with norm ns.
    
    # We only have to check up to the square root, larger than that and the norm is guaranteed to be more than ns.
    n=int(numpy.ceil(numpy.sqrt(ns)))+1 
    # To save time we don't have to check from -n to n for each variable.  We can just do
    return [ [x, y, z] for x in range(n) for y in range(x,n) for z in range(y,n) if x*x + y*y + z*z == ns ]
    # and then use symmetry_image to generate all possible cubic rotations.

def shape(vec):
    vec.sort()
    [x,y,z] = vec
    if x==0 and y==0 and z==0:  
        return "point"
    if x==0 and y==0:
        return "octahedron"
    if x==0 and y==z:
        return "cuboctahedron"
    if x==0 and y!=z:
        return "truncated octahedron"
    if x==y and x==z:
        return "cube"
    if (x==y and x!=z) or (x!=y and y==z):
        return "small rhombicuboctahedron"
    if x!=y and x!=z and y!=z:
        return "great rhombicuboctahedron"
    return "?"