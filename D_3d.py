import symmetry
import numpy

# D_3d is the symmetry of a cube that's squashed along the direction of a cubic diagonal.
# It's made out of six identical rhombi.

# Such a shape is also called a triangular antiprism or a trigonal trapzeohedron.

# The first symmetry is the trivial one, the do-nothing operation.
identity = symmetry.Class("E", [ symmetry.identity ],
    {   "A1g":  +1,
        "A2g":  +1,
        "Eg":   +2,
        "A1u":  +1,
        "A2u":  +1,
        "Eu":   +2,
    } )

# There is also the point-inversion.
inversion = symmetry.Class("i", [ symmetry.inversion ],
    {   "A1g":  +1,
        "A2g":  +1,
        "Eg":   +2,
        "A1u":  +1,
        "A2u":  +1,
        "Eu":   +2,
    })

# There's a three-fold symmetry around the squashed axis:
diagonal_rotation = symmetry.Class("2C_3", 
    [
        symmetry.Rotation([+1,+1,+1], +2*numpy.pi/3),
        symmetry.Rotation([+1,+1,+1], -2*numpy.pi/3)
    ],
    {   "A1g":  +1,
        "A2g":  +1,
        "Eg":   -1,
        "A1u":  +1,
        "A2u":  +1,
        "Eu":   -1,
    }
)

# There's the improper version of the same:
diagonal_improper = symmetry.Class("2S_6",
    [ op * symmetry.inversion for op in diagonal_rotation.ops ],
    {   "A1g":  +1,
        "A2g":  +1,
        "Eg":   -1,
        "A1u":  -1,
        "A2u":  -1,
        "Eu":   +1,
    }
)

# Finally, there are three very-hard-to-see 180-degree rotations that pierce the edges that don't touch the "squashed" corners...
edge_rotation = symmetry.Class("3C'_2",
    [
        symmetry.Rotation([ +1,  0, -1], +numpy.pi),
        symmetry.Rotation([ +1, -1,  0], +numpy.pi),
        symmetry.Rotation([  0, +1, -1], +numpy.pi)
    ],
    {   "A1g":  +1,
        "A2g":  -1,
        "Eg":    0,
        "A1u":  +1,
        "A2u":  -1,
        "Eu":    0,
    }
)

# ... and associated reflections.
edge_reflection = symmetry.Class("3sigma_d",
    [   rot * symmetry.inversion for rot in edge_rotation.ops    ],
    {   "A1g":  +1,
        "A2g":  -1,
        "Eg":    0,
        "A1u":  -1,
        "A2u":  +1,
        "Eu":    0,
    }
)

# The D_2h group is the collection of all of those symmetry actions.
group = symmetry.Group("D_2h",
    [
        identity,   diagonal_rotation, edge_rotation,
        inversion,  diagonal_improper, edge_reflection
    ],
    [ "A1g", "A2g", "Eg", "A1g", "A2u", "Eu" ]
)