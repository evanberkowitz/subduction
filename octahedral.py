import symmetry
import numpy

# The cube has many symmetries.

# The first is the trivial one, the do-nothing operation.
identity = symmetry.Class("E", [ symmetry.Reflection([+1,+1,+1]) ] )

# We can skewer a cube through its inner diagonals.  There's three-fold symmetry around those axes.
corners = symmetry.Class(
    "8C_3",
    [
        symmetry.Rotation([+1,+1,+1], 2*numpy.pi/3),
        symmetry.Rotation([+1,+1,+1], 4*numpy.pi/3),
        symmetry.Rotation([+1,+1,-1], 2*numpy.pi/3),
        symmetry.Rotation([+1,+1,-1], 4*numpy.pi/3),
        symmetry.Rotation([+1,-1,+1], 2*numpy.pi/3),
        symmetry.Rotation([+1,-1,+1], 4*numpy.pi/3),
        symmetry.Rotation([+1,-1,-1], 2*numpy.pi/3),
        symmetry.Rotation([+1,-1,-1], 4*numpy.pi/3),
    ]
)

# We can pick two opposite edges and skewer through their midpoints.  There's two-fold symmetry around those axes.
edges = symmetry.Class(
    "6C_2",
    [
        symmetry.Rotation([ 0,+1,+1], numpy.pi),
        symmetry.Rotation([ 0,-1,+1], numpy.pi),
        symmetry.Rotation([+1, 0,+1], numpy.pi),
        symmetry.Rotation([-1, 0,+1], numpy.pi),
        symmetry.Rotation([+1,+1, 0], numpy.pi),
        symmetry.Rotation([+1,-1, 0], numpy.pi),
    ]
)

# We can skewer right through the faces and do 180-degree rotations...
face_180 = symmetry.Class(
    "3C_2",
    [
        symmetry.Rotation([1,0,0], numpy.pi),
        symmetry.Rotation([0,1,0], numpy.pi),
        symmetry.Rotation([0,0,1], numpy.pi),
    ]
)

# ... or 90-degree rotations
face_090 = symmetry.Class(
    "6C_4",
    [
        symmetry.Rotation([1,0,0], +numpy.pi/2),
        symmetry.Rotation([1,0,0], -numpy.pi/2),
        symmetry.Rotation([0,1,0], +numpy.pi/2),
        symmetry.Rotation([0,1,0], -numpy.pi/2),
        symmetry.Rotation([0,0,1], +numpy.pi/2),
        symmetry.Rotation([0,0,1], -numpy.pi/2),
    ]
)

# We can do a point reflection, sending every point to its additive inverse.
inv = symmetry.Reflection([-1,-1,-1])
inversion = symmetry.Class("i", [ inv ])

# We can put mirrors through the origin, parallel to the faces.
# These are equivalent to doing a 180-degree face rotation after an inversion.
axis_reflection = symmetry.Class("3sigma_h",
    [
        symmetry.Reflection([-1,+1,+1]),
        symmetry.Reflection([+1,-1,+1]),
        symmetry.Reflection([+1,+1,-1])
    ]
)

# We can put mirrors through opposite facial diagonals.
diagonal_reflection = symmetry.Class("6sigma_d",
    [ rot*inv for rot in edges.ops ]
)

# And we can combine a point reflection with the edge rotations...
inverted_edges = symmetry.Class("6S_4",
    [ rot*inv for rot in face_090.ops ]
)

# ... and corner rotations.
inverted_corners = symmetry.Class("8S_4",
    [ rot*inv for rot in corners.ops ]
)

# The octahedral group is the collection of all of those symmetry actions.
group = symmetry.Group("O_H",
    [
        identity, corners, edges, face_180, face_090, inversion, axis_reflection, diagonal_reflection, inverted_edges, inverted_corners
    ]
)