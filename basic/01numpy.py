import numpy as np

# set seed for reproducibility
np.random.seed(seed=6)


#matrix

#make a 3-D array
x = np.array([[[1,2,3], [4, 5, 6]]])
print(x)
'''
dimension, count of square bracket
'''
print('x.ndim', x.ndim)
'''
shape, item count after removing outer square bracket
'''
print('x.shape', x.shape)
'''
iten count
'''
print('x.size', x.size)
'''
item type
'''
print('x.dtype', x.dtype)


#functions

print('np.zeros', np.zeros((2,3)))
print('np.ones', np.ones((2,3)))
print('np.eye', np.eye(3))
print('np.random.random', np.random.random((2,3)))


#indexing
x = np.array([1, 2, 3])
print('x[0]', x[0])
x[0] = 0
print(x)

#slicing
x = np.array([[1, 2, 3], [4, 5, 6]])
print('x', x)
print('x column 1:', x[:, 1])
print('x row 0:', x[0, :])
print('x column 0, 1', x[:, :2])

#integer array indexing

'''
len is equal to shape[0]
'''
rows2get = np.arange(len(x))
cols2get = np.array([0, 2])

print('x', x)
print('rows to get', rows2get)
print('cols to get', cols2get)
print('get info', x[rows2get, cols2get])

#boolean array indexing
x = np.array([[1, 2], [3, 4]])
print ('x:', x)
print('x>2: ', x>2)
print('x[x>2]', x[x>2])

#array math
x = np.array([[1, 2], [3, 4]])
y = np.array([[4, 5], [6, 7]])
print('x+y: ', np.add(x, y))
print('x-y: ', np.subtract(x, y))
print('x*y: ', np.multiply(x, y))

#dot product
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8], [9, 10], [10, 11]])
print('a.dot(b)', a.dot(b))

#sum across dimension
print('a', a)
print('sum all', np.sum(a))
print('sum column', np.sum(a, axis=0))
print('sum row', np.sum(a, axis=1))

#transpose
print('a.T', a.T)

#tile
'''
np.tile(A, reps)
Construct an array by repeating A the number of times given by reps
'''
a = np.array([1, 2, 3, 4])
print('a', a)
print('np.tile(a, 2)', np.tile(a, 2))
print('np.tile(a, (2, 2))', np.tile(a, (2, 2)))


#broadcasting
a = np.array([[1, 2], [3, 4]])
b = np.array([5, 6])
print('a+b', a+b)

#reshaping
x = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
print('x', x, x.shape)
y = np.reshape(x, (2, -1))
print('y', y, y.shape)

#removing dimensions
'''
numpy.squeeze(a, axis=None)
Remove single-dimensional entries from the shape of an array
'''
a = np.array([[[1,2], [3, 4]]])
print('a', a, a.shape)
b = np.squeeze(a, 0)
print('b', b, b.shape)

#adding dimensions
x = np.array([[1,2,1],[2,2,3]])
print ("x.shape: ", x.shape)
y = np.expand_dims(x, 1) # expand dim 1
print ("y.shape: ", y.shape) 
print ("y: \n", y)

