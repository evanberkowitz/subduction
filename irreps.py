import numpy
import itertools
from scipy.special import sph_harm



def nsq(ns):
    # Returns a list of all the vectors with nondecreasing, nonnegative integer entries with norm ns.
    
    # We only have to check up to the square root, larger than that and the norm is guaranteed to be more than ns.
    n=int(numpy.ceil(numpy.sqrt(ns)))+1 
    # To save time we don't have to check from -n to n for each variable.  We can just do
    return [ [x, y, z] for x in range(n) for y in range(x,n) for z in range(y,n) if x*x + y*y + z*z == ns ]
    # and then use symmetry_image to generate all possible cubic rotations.

def vec_to_angles(vec):
    # Returns a dictionary of angles.  The azimuthal lies in [0, 2*pi], the polar in [0,pi].
    norm=numpy.sqrt(reduce( numpy.add, [x*x for x in vec],0))
    azimuthal=numpy.arctan2(vec[1],vec[0])
    polar=numpy.arcsin(vec[2]/norm)
    return { 'azimuthal':azimuthal, 'polar':polar }

def Ylm(l,m):
    # Returns a function that takes a vector and returns Ylm in that direction.
    def partial_wave(vec):
        angles=vec_to_angles(vec)
        return sph_harm(m,l,angles['azimuthal'],angles['polar'])
    return partial_wave