import symmetry
import numpy

# D4h is the symmetry of a rectangular prism where one direction is compressed compared to the other two.

# The picture looks kind of like this:
#       
#       
#              +-----+
#             /     /|
#            /     / |
#           /  x  /  |
#          /  x  /   |
#         /     /    |
#        /     /     |
#       +-----+      |
#       |     |  zz  |
#       |     |      +
#       |     |     /
#       |  y  |    /
#       |     |   /
#       |     |  /
#       |     | /
#       |     |/
#       +-----+

# The first is the trivial one, the do-nothing operation.
identity = symmetry.Class("E", [ symmetry.identity ],
    {   "A1g":  +1,
        "A2g":  +1,
        "B1g":  +1,
        "B2g":  +1,
        "Eg":   +2,
        "A1u":  +1,
        "A2u":  +1,
        "B1u":  +1,
        "B2u":  +1,
        "Eu":   +2
    } )

# Then, we can rotate around the z axis.  we can rotate 180-degrees...
z_face_180 = symmetry.Class("C_2",   [   symmetry.Rotation([0,0,1], numpy.pi)    ],
    {   "A1g":  +1,
        "A2g":  +1,
        "B1g":  +1,
        "B2g":  +1,
        "Eg":   -2,
        "A1u":  +1,
        "A2u":  +1,
        "B1u":  +1,
        "B2u":  +1,
        "Eu":   -2
    } )

# or we can rotate ±90-degrees
z_face_90 = symmetry.Class("2C_4(z)",
    [   
        symmetry.Rotation([0,0,1], +numpy.pi/2),
        symmetry.Rotation([0,0,1], -numpy.pi/2),
    ],
    {   "A1g":  +1,
        "A2g":  +1,
        "B1g":  -1,
        "B2g":  -1,
        "Eg":    0,
        "A1u":  +1,
        "A2u":  +1,
        "B1u":  -1,
        "B2u":  -1,
        "Eu":    0
    } )

# // TODO: it's important to make sure the characters are right.  I'm not 100% sure.  edges' characters may be switched with faces'.
# We can skewer two opposing short edges and rotate by 180 degrees.
edges = symmetry.Class("2C'_2",
    [
        symmetry.Rotation([+1,+1,0], numpy.pi),
        symmetry.Rotation([+1,-1,0], numpy.pi)
    ],
    {   "A1g":  +1,
        "A2g":  -1,
        "B1g":  -1,
        "B2g":  +1,
        "Eg":    0,
        "A1u":  +1,
        "A2u":  -1,
        "B1u":  -1,
        "B2u":  +1,
        "Eu":    0,
    }
)

# We can skewer two opposing rectangular faces and rotate by 180 degrees (x- and y-axes)
faces = symmetry.Class("2C''_2",
    [
        symmetry.Rotation([1,0,0], numpy.pi),
        symmetry.Rotation([0,1,0], numpy.pi)
    ],
    {   "A1g":  +1,
        "A2g":  -1,
        "B1g":  +1,
        "B2g":  -1,
        "Eg":    0,
        "A1u":  +1,
        "A2u":  -1,
        "B1u":  +1,
        "B2u":  -1,
        "Eu":    0,
    }
)


# We can do a point reflection around the origin:
inversion = symmetry.Class("i",
    [   symmetry.inversion  ],
    {   "A1g":  +1,
        "A2g":  +1,
        "B1g":  +1,
        "B2g":  +1,
        "Eg":   +2,
        "A1u":  -1,
        "A2u":  -1,
        "B1u":  -1,
        "B2u":  -1,
        "Eu":   -2,
    }
)

# We can reflect across the xy-plane:
z_reflection = symmetry.Class(
    "sigma_h",
    [ symmetry.Reflection([+1,+1,-1]) ],
    {   "A1g":  +1,
        "A2g":  +1,
        "B1g":  +1,
        "B2g":  +1,
        "Eg":   -2,
        "A1u":  -1,
        "A2u":  -1,
        "B1u":  -1,
        "B2u":  -1,
        "Eu":   +2,
    }
)

# We can reflect across the xy-plane and do a ±90 degree turn:
z_face_90_inv = symmetry.Class(
    "2S_4",
    [ rot * symmetry.inversion for rot in z_face_90.ops ],
    {   "A1g":  +1,
        "A2g":  +1,
        "B1g":  -1,
        "B2g":  -1,
        "Eg":    0,
        "A1u":  -1,
        "A2u":  -1,
        "B1u":  +1,
        "B2u":  +1,
        "Eu":    0,
    }
)

# We can reflect across a plane that contains two opposite short edges:
edges_inv = symmetry.Class(
    "2sigma_d",
    [ rot * symmetry.inversion for rot in edges.ops ],
    {   "A1g":  +1,
        "A2g":  -1,
        "B1g":  -1,
        "B2g":  +1,
        "Eg":    0,
        "A1u":  -1,
        "A2u":  +1,
        "B1u":  +1,
        "B2u":  -1,
        "Eu":    0,
    }
)

# We can reflect across the xz and yz planes:
faces_inv = symmetry.Class(
    "2sigma_v",
    [ rot * symmetry.inversion for rot in faces.ops ],
    {   "A1g":  +1,
        "A2g":  -1,
        "B1g":  +1,
        "B2g":  -1,
        "Eg":    0,
        "A1u":  -1,
        "A2u":  +1,
        "B1u":  -1,
        "B2u":  +1,
        "Eu":    0,
    }
)

# The D_4h group is the collection of all of those symmetry actions.
group = symmetry.Group("D_4h",
    [
        identity,   z_face_180,   z_face_90,        edges,      faces,
        inversion,  z_reflection, z_face_90_inv,    edges_inv,  faces_inv
    ],
    [ "A1g", "A2g", "B1g", "B2g", "Eg", "A1u", "A2u", "B1u", "B2u", "Eu" ],
)