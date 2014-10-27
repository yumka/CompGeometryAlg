__author__ = 'yumka'

# Compute convex hull for a set of points
# Example with Graham Scan algorithm implemented by Tom Switzer <thomas.switzer@gmail.com>
# Extended with alternative criterion for testing point turns
import numpy as np
import matplotlib.pyplot as plt

n = 100
x_coord = np.random.random([n])
y_coord = np.random.random([n])
# Make pairs
points = zip(x_coord,y_coord)


# Graham Scan - Tom Switzer <thomas.switzer@gmail.com>
TURN_LEFT, TURN_RIGHT, TURN_NONE = (1, -1, 0)

def turn(p, q, r):
#cmp- compare two objects and return an integer 1 if first is bigger, -1 if smaller, and 0 if equal
    return cmp((q[0] - p[0])*(r[1] - p[1]) - (r[0] - p[0])*(q[1] - p[1]), 0)
#Alternative criterion for testing turn, #yumka
def turn2(p, q, r):
    return cmp((q[0] - p[0])*(r[1] - q[1]) - (r[0] - q[0])*(q[1] - p[1]), 0)

def _keep_left(hull, r):
    while len(hull) > 1 and turn2(hull[-2], hull[-1], r) != TURN_LEFT:
            hull.pop()
    if not len(hull) or hull[-1] != r:
        hull.append(r)
    return hull

def convex_hull(points):
    """Returns points on convex hull of an array of points in CCW order."""
    points = sorted(points)
    # Function reduce takes starting value ([]) and first elements of array "points" and passes to function
    #_keep_left. Then it takes result of function _take_left and passes it again to the function _take_left
    # with the next element of array "points" and so on.

    l = reduce(_keep_left, points, [])
    u = reduce(_keep_left, reversed(points), [])
    # Extend l (lower hull) with all elements of u(upper hull) excluding its first and last elements
    # it reads from left to right, if first element is true it returns it
    return l.extend(u[i] for i in xrange(1, len(u) - 1)) or l


ch = (convex_hull(points))
# Divide list into separate tuples
ch_unzip= zip(*ch)

# Add a single element into tuple
ch_unzip[0]= ch_unzip[0] + (ch_unzip[0][0],)
ch_unzip[1]= ch_unzip[1]+ (ch_unzip[1][0],)

# Plot points and convex hull
plt.plot(x_coord, y_coord,'ro')
plt.plot(ch_unzip[0],ch_unzip[1],'r')
plt.axis([-0.5, 1.5, -0.5, 1.5])
plt.show()

