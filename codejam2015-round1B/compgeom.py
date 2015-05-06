from math import sqrt,floor,ceil,log,log10,exp,sin,cos,tan,asin,acos,atan2
from math import pi as PI

inf = float('inf')

DEBUG = True

def vadd(v1,v2):
    '''Returns v1+v2.'''
    return [a+b for a,b in zip(v1,v2)]

def vsub(v1,v2):
    '''Returns v1-v2.'''
    return [a-b for a,b in zip(v1,v2)]

def smul(c,v):
    '''Returns the scalar c multiplied by the vector v.'''
    return [c*a for a in v]

def dot(v1,v2):
    '''Returns the Euclidean inner product of v1 and v2.'''
    return sum([a*b for a,b in zip(v1,v2)])

def norm(v,p=2):
    '''Returns the Euclidean L^p norm of v, where p is presumed to be 2
unless otherwise specified. p may range from 1 to +inf.'''
    if p == 2: return sqrt(dot(v,v))
    elif p == inf: return max([abs(a) for a in v])
    elif p >= 1: return sum([abs(a)**p for a in v])**(1.0/p)
    else: raise ValueError, 'p must be in the range [1,+inf]'

def angle(v1,v2):
    '''Returns an angle between 0 and PI, with PI/2 meaning the v1 and v2 are
orthogonal.'''
    return acos(dot(v1,v2)/(norm(v1)*norm(v2)))

def unit(v):
    '''Returns a unit vector with the same direction as v. Return None if v is
the zero vector.'''
    if set(v) == set([0]): return None
    return smul(1./norm(v),v)

def cross(v1,v2):
    if len(v1) == len(v2) == 2:
        a,c = v1
        b,d = v2
        return [0,0,a*d-b*c]
    elif len(v1) == len(v2) == 3:
        x1,y1,z1 = v1
        x2,y2,z2 = v2
        return [y1*z2-y2*z1,z1*x2-z2*x1,x1*y2-x2*y1]
    else: raise TypeError, 'v1 and v2 should both be dimension 2 or both be dimension 3'

def ptPtDist(p,q):
    '''Given two points in R^k, returns the distance between p and q.'''
    return norm(vsub(p,q))

def midpt(p,q):
    return smul(0.5,vadd(p,q))

def lineIntersectR2(v1,p1,v2,p2):
    '''Given a vector v1 in the direction of line L1 in R^2 and a point p1
on L1 and a vector v2 in the direction of line L2 and a point on L2,
returns the point q in R^2 that is the intersection of the two lines. If
L1 and L2 are parallel, returns None. If L1 == L2, returns the midpoint
of the segment from p1 to p2.'''
    dx1,dy1 = v1
    dx2,dy2 = v2
    x1,y1 = p1
    x2,y2 = p2
    # L1 is:
    #    dx1 * (y-y1) - dy1 * (x-x1) == 0
    #    -dy1 * x + dx1 * y == (-dy1*x1 + dx1*y1)
    # L2 is:
    #    dx2 * (y-y2) - dy2 * (x-x2) == 0
    #    -dy2 * x + dx2 * y == (-dy2*x2 + dx2*y2)
    # their intersection is given by solving the system of equations
    #    [-dy1 dx1  [ x   = [ -dy1*x1 + dx1*y1
    #     -dy2 dx2 ]  y ]     -dy2*x2 + dx2*y2 ]
    #    [ x   =  1/(-dy1*dx2 + dy2*dx1) * [ dx2 -dx1   [-dy1*x1 + dx1*y1
    #      y ]                               dy2 -dy1 ]  -dy2*x2 + dx2*y2 ]
    #          =  1/(dx1*dy2 - dx2*dy1) * [-dx2*dy1*x1 + dx1*dx2*y1 + dx1*dy2*x2 - dx1*dx2*y2 
    #                                      -dy1*dy2*x1 + dx1*dy2*y1 + dy1*dy2*x2 - dx2*dy1*y2 ]
    det = 1.0*(dx1*dy2 - dx2*dy1)
    if det == 0:
        dx3,dy3 = vsub(p1,p2)
        if dx1*dy3 - dx3*dy1: # p1-p2 is parallel to the line means that they define the same line
            return midpt(p1,p2)
        else:
            return None
    x = (-dx2*dy1*x1 + dx1*dx2*y1 + dx1*dy2*x2 - dx1*dx2*y2)/det
    y = (-dy1*dy2*x1 + dx1*dy2*y1 + dy1*dy2*x2 - dx2*dy1*y2)/det
    return [x,y]

def ptLineDistR2(v,p,q):
    '''Given a vector v in the direction of a line in R^2, a point p in R^2 on
the line, and a point q in R^2, returns the distance from q to the line.'''
    dx,dy = v
    x0,y0 = p
    x1,y1 = q
    w = -dy,dx
    # the line perpendicular to v passing through p is:
    #    dy * (y-y1) + dx * (x-x1) == 0
    #    dx * x + dy * y == (dx*x1 + dy*y1)
    # the original line is:
    #    dx * (y-y0) - dy * (x-x0) == 0
    #    -dy * x + dx * y == (-dy*x0 + dx*y0)
    # their intersection is given by solving the system of equations
    #    [ dx dy  [ x   = [ dx*x1 + dy*y1
    #     -dy dx ]  y ]    -dy*x0 + dx*y0 ]
    #    [ x   =  1/(dx**2 + dy**2) * [ dx -dy   [ dx*x1 + dy*y1
    #      y ]                          dy  dx ]  -dy*x0 + dx*y0 ]
    #          =  1/(dx**2 + dy**2) * [ dx**2*x1 + dx*dy*y1 + dy**2*x0 - dx*dy*y0 
    #                                   dy*dx*x1 + dy**2*y1 - dx*dy*x0 + dx**2*y0 ]
    intersection = lineIntersectR2(v,p,w,q)
##    intersection = [(dx**2*x1 + dx*dy*y1 + dy**2*x0 - dx*dy*y0)/M,
##                    (dy*dx*x1 + dy**2*y1 - dx*dy*x0 + dx**2*y0)/M]
    return ptPtDist(q,intersection)

# from https://www.topcoder.com/community/data-science/data-science-tutorials/geometry-concepts-basic-concepts/
def areaOfPolygon(pts):
    '''Given pts, a list of the vertices of a polygon in R^2 ordered so
consecutive vertices are adjacent and the first and last vertices are
adjacent, returns the (signed) area of the polygon. (Negative area means
that the polygon's vertices were ordered clockwise.)'''
    area = 0
    N = len(pts)
    # triangulate the polygon into triangles with points pts[0], pts[i],
    # and pts[i+1]
    p0 = pts[0]
    for i in range(1,N-1):
        v1 = vsub(pts[i],p0)
        v2 = vsub(pts[i+1],p0)
        area += cross(v1,v2)[2]/2.0
    return area

# test cases
if DEBUG:
    eps = 10**-6
    
    assert vadd([1],[1]) == [2]
    assert vadd([1,2],[2,1]) == [3,3]

    assert vsub([1],[1]) == [0]
    assert vsub([1,2],[2,1]) == [-1,1]

    assert smul(1,[2,3]) == [2,3]
    assert smul(0,[2,3]) == [0,0]
    assert smul(-1,[2,3]) == [-2,-3]

    assert abs(dot([1,1],[-1,1]) - 0) <= eps
    assert abs(dot([1,1],[1,1]) - 2) <= eps

    assert abs(norm([1,1]) - sqrt(2)) <= eps
    assert abs(norm([0,0]) - 0) <= eps
    assert abs(norm([1,1,1,1]) - 2) <= eps

    assert norm([1,1,-2,1],p=1) == 5
    assert norm([1,1,-2,1],p=inf) == 2

    assert abs(angle([1,1],[-1,1]) - PI/2) <= eps
    assert abs(angle([1,1],[2,2]) - 0) <= eps
    assert abs(angle([1,1],[-2,-2]) - PI) <= eps
    assert abs(angle([1,0],[1,1]) - PI/4) <= eps

    assert unit([-2]) == [-1]
    assert unit([0,0]) is None
    assert unit([1,0,1]) == [1./sqrt(2),0,1./sqrt(2)]

    assert cross([1,1],[2,2]) == [0,0,0]
    assert cross([1,0],[0,1]) == [0,0,1]
    assert cross([2,3],[-1,2]) == [0,0,7]
    
    assert cross([1,1,1],[3,3,3]) == [0,0,0]
    assert cross([1,0,0],[0,1,0]) == [0,0,1]
    assert cross([1,2,3],[1,1,1]) == [-1,2,-1]

    assert abs(ptPtDist([1,1],[0,0]) - sqrt(2)) <= eps
    assert abs(ptPtDist([1,1,1],[1,0,1]) - 1) <= eps

    assert abs(ptLineDistR2([1,0],[2,1],[-1,-1]) - 2) <= eps
    assert abs(ptLineDistR2([-2,0],[2,1],[-1,-1]) - 2) <= eps

    assert abs(areaOfPolygon([[-1,0],[0,1],[1,0],[0,-1],[0,0]]) + 1.5) <= eps
