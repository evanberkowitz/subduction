import symmetry
import numpy

# D_2h is the symmetry of a rectangular prism where all three side lengths are different.

# It is also the symmetry of a cube that has been squashed along a facial diagonal, which is made of two parallel rhombi joined by four congruent rectangles.
# Such a shape is called a right rhombic prism, and can serve as a unit cell for the orthorhombic Bravais lattice.

# The first is the trivial one, the do-nothing operation.
identity = symmetry.Class("E", [ symmetry.identity ],
    {   "Ag":   +1,
        "B1g":  +1,
        "B2g":  +1,
        "B3g":  +1,
        "Au":   +1,
        "B1u":  +1,
        "B2u":  +1,
        "B3u":  +1,
    } )

# There is also the point-inversion.
inversion = symmetry.Class("i", [ symmetry.inversion ],
    {   "Ag":   +1,
        "B1g":  +1,
        "B2g":  +1,
        "B3g":  +1,
        "Au":   -1,
        "B1u":  -1,
        "B2u":  -1,
        "B3u":  -1,
    })

x_rotation = symmetry.Class("C_2(x)",
    [ symmetry.Rotation([1,0,0], numpy.pi) ],
    {   "Ag":   +1,
        "B1g":  -1,
        "B2g":  -1,
        "B3g":  +1,
        "Au":   +1,
        "B1u":  -1,
        "B2u":  -1,
        "B3u":  +1,
    }
)

y_rotation = symmetry.Class("C_2(y)",
    [ symmetry.Rotation([0,1,0], numpy.pi) ],
    {   "Ag":   +1,
        "B1g":  -1,
        "B2g":  +1,
        "B3g":  -1,
        "Au":   +1,
        "B1u":  -1,
        "B2u":  +1,
        "B3u":  -1,
    }
)

z_rotation = symmetry.Class("C_2(z)",
    [ symmetry.Rotation([0,0,1], numpy.pi) ],
    {   "Ag":   +1,
        "B1g":  +1,
        "B2g":  -1,
        "B3g":  -1,
        "Au":   +1,
        "B1u":  +1,
        "B2u":  -1,
        "B3u":  -1,
    }
)

x_reflection = symmetry.Class("sigma(yz)",
    [ symmetry.Reflection([-1,+1,+1]) ],
    {   "Ag":   +1,
        "B1g":  -1,
        "B2g":  -1,
        "B3g":  +1,
        "Au":   -1,
        "B1u":  +1,
        "B2u":  +1,
        "B3u":  -1,
    }
)

y_reflection = symmetry.Class("sigma(zx)",
    [ symmetry.Reflection([+1,-1,+1]) ],
    {   "Ag":   +1,
        "B1g":  -1,
        "B2g":  +1,
        "B3g":  -1,
        "Au":   -1,
        "B1u":  +1,
        "B2u":  -1,
        "B3u":  +1,
    }
)

z_reflection = symmetry.Class("sigma(xy)",
    [ symmetry.Reflection([+1,+1,-1]) ],
    {   "Ag":   +1,
        "B1g":  +1,
        "B2g":  -1,
        "B3g":  -1,
        "Au":   -1,
        "B1u":  -1,
        "B2u":  +1,
        "B3u":  +1,
    }
)


# The D_2h group is the collection of all of those symmetry actions.
group = symmetry.Group("D_2h",
    [
        identity,   x_rotation,     y_rotation,     z_rotation,     
        inversion,  x_reflection,   y_reflection,   z_reflection,   
    ],
    { "Ag": 1, "B1g": 1, "B2g": 1, "B3g":1, "Au": 1, "B1u": 1, "B2u":1 , "B3u":1 },
)