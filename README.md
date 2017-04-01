# `subduction`

Suite for subducing output of LQCD computations to definite cubic irreps.

# Introduction

Our world exhibits rotational symmetry.  By Noether's theorem we are guaranteed that angular momentum is a conserved quantum number.

Lattice QCD is a technique for extracting first-principles predictions from QCD, the theory of quarks and gluons, in the regime where pen-and-paper methods are unreliable because of strong coupling.  Lattice QCD is usually performed on a (four-dimensional) hypercubic grid.  To maintain (a discrete subset of) translational invariance, we typically apply periodic boundary conditions to this lattice.  So, to make life easy, we make the whole grid hypercubic as well.

However, this introduces a problem---our spatial volume only has discrete rotational symmetry---the rotations of a cube---rather the the complete rotational symmetry.  This implies that angular momentum is no longer a good, conserved quantum number.  Instead, there is another quantum number that labels the irreducible representations of the discrete rotational symmetry.

Using output from our lattice computations, we need to construct these irreducible representations.  Only then can we apply Lüscher's formula and get at infinite-volume scattering data.