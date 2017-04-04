from __future__ import print_function
import os, sys
import argparse
import irreps
import octahedral

print( octahedral.group )

print("nsquared table")
[ print(n,len(irreps.nsq(n)), [ len(octahedral.group.on(i)) for i in irreps.nsq(n) ] ,irreps.nsq(n)) for n in range(20) ]
