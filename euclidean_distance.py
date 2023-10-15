"""Create a folder named day_1 inside 30DaysOfPython folder. 
Inside day_1 folder, create a python file helloworld.py 
and repeat questions 1, 2, 3 and 4. Remember to use print() 
when you are working on a python file. 
Navigate to the directory where you have saved your file, and run it.
Exercise: Level 3

Write an example for different Python data types such as
 Number(Integer, Float, Complex), String, Boolean, List, 
 Tuple, Set and Dictionary.
Find an Euclidian distance between (2, 3) and (10, 8)"""

from math import sqrt

name = 'Ryan'
print('Name is', name)

point_p = (2, 3)
point_q = (10, 8)
# p: (p1,p2), q: (q1,q2)
# d(p,q) = sqrt((q1-p1)^2+(q2-p2)^2)

print('Distance between points (2,3) and (10,8) is:', 
      sqrt(((point_q[0]-point_p[0])**2)+(point_q[1]-point_p[1])**2))