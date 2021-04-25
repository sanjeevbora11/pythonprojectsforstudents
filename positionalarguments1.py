'''
WAP to calculate Volume of Cube and Cuboid.
Define functions for both.
'''
def VolCube(side):
    v=side*side*side
    return v
def VolCuboid(l,b,h):
    vol=l*b*h
    return vol
print(VolCuboid(2,3,4))
print(VolCuboid(3,4,5))
