""" Write a Python script that displays the following table
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125

1, 1^0, 1^1, 1^2, 1^3
2, 2^0, 2^1, 2^2, 2^3
3, 3^0, 3^1, 3^2, 3^3
4, 4^0, 4^1, 4^2, 4^3
5, 5^0, 5^1, 5^2, 5^3
"""

table = [1,2,3,4,5]
for n in table:
    print(n,n**0,n**1,n**2,n**3)