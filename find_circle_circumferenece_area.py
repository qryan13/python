# Enter a value in radius to return the area and circumference of the corresponding circle.
# default unit is set to meters
import math

radius = input('Enter the radius in meters: ')
area_circle = (math.pi * (int(radius) ** 2))
print('The area of the circle is', area_circle, 'meters')
circumference_circle = (2 * math.pi * int(radius))
print('The circumference of the circle is ', circumference_circle, 'meters')

