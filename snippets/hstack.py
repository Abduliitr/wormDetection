import numpy as np

# hstack is horizontal stack
# i.e., Stack arrays in sequence horizontally (column wise).

# This is equivalent to concatenation along the second axis, except for 1-D arrays where it concatenates along the first axis. Rebuilds arrays divided by hsplit.

# numpy.hstack(sequence of ndarrays)  --> returns stacked : ndarray

a = np.array((1,2,3))
print(a)
b = np.array((2,3,4))
print(b)
c = np.hstack((a,b))
print(c)
#  array([1, 2, 3, 2, 3, 4])
print("--------------")
a = np.array([[1],[2],[3]])
print(a)
b = np.array([[2],[3],[4]])
print(b)
d = np.hstack((a,b))
print(d)
#  array([[1, 2],[2, 3],[3, 4]])