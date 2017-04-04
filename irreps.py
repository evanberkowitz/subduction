import numpy
import itertools
from scipy.special import sph_harm



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
    
def nsq_character():
    return None

def nsq_degeneracy(group):
    return { irrep: 1 for irrep in group.irreps.keys() }