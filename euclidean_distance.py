# Find an Euclidian distance between two points

from math import sqrt

point_p = (2, 3)
point_q = (10, 8)

# d(p,q) = sqrt((q1-p1)^2+(q2-p2)^2)
print('Distance between points (2,3) and (10,8) is:', 
     sqrt(((point_q[0]-point_p[0])**2)+(point_q[1]-point_p[1])**2))
