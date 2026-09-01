import numpy as np

# ==========================================================
# NUMPY TUTORIAL - FULL NOTES
# ==========================================================


# ----------------------------------------------------------
# NumPy HOME
# ----------------------------------------------------------
# NumPy = Numerical Python, used for working with arrays.
# It is much faster than Python lists.

# ----------------------------------------------------------
# NumPy Intro
# ----------------------------------------------------------
# NumPy provides an array object called ndarray.
print(np.__version__)


# ----------------------------------------------------------
# NumPy Getting Started
# ----------------------------------------------------------
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))


# ----------------------------------------------------------
# NumPy Creating Arrays
# ----------------------------------------------------------
arr0 = np.array(42)                 # 0-D array
arr1 = np.array([1, 2, 3, 4])       # 1-D array
arr2 = np.array([[1, 2], [3, 4]])   # 2-D array
arr3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])  # 3-D array
print(arr0, arr1, arr2, arr3)
print(arr3.ndim)  # number of dimensions

# arrays with a defined number of dimensions
arr5 = np.array([1, 2, 3, 4], ndmin=5)
print(arr5)
print('shape:', arr5.shape)


# ----------------------------------------------------------
# NumPy Array Indexing
# ----------------------------------------------------------
arr = np.array([1, 2, 3, 4])
print(arr[0])       # 1
print(arr[2] + arr[3])  # 7

arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2d[1, 4-3])  # element on row 1, col 1 -> 5

arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr3d[0, 1, 1])  # 4

arr = np.array([1, 2, 3, 4])
print(arr[-1])  # negative indexing -> 4


# ----------------------------------------------------------
# NumPy Array Slicing
# ----------------------------------------------------------
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])     # [2 3 4 5]
print(arr[4:])       # [5 6 7]
print(arr[:4])       # [1 2 3 4]
print(arr[-3:-1])    # [5 6]
print(arr[1:5:2])    # step -> [2 4]
print(arr[::2])      # every other element

arr2d = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr2d[1, 1:4])   # [7 8 9]
print(arr2d[0:2, 2])   # [3 8]
print(arr2d[0:2, 1:4]) # from both rows, col 1 to 3


# ----------------------------------------------------------
# NumPy Data Types
# ----------------------------------------------------------
arr = np.array([1, 2, 3, 4])
print(arr.dtype)  # int64 / int32

arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)  # <U6 (string)

arr = np.array([1, 2, 3, 4], dtype='S')  # define data type
print(arr, arr.dtype)

arr = np.array([1, 2, 3, 4], dtype='i4')  # 4 byte integer
print(arr, arr.dtype)

# converting data type on existing array
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
print(newarr, newarr.dtype)

arr = np.array([1, 0, 3])
newarr = arr.astype(bool)
print(newarr)


# ----------------------------------------------------------
# NumPy Copy vs View
# ----------------------------------------------------------
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()   # copy owns the data
arr[0] = 42
print(arr, x)  # x is unaffected

arr = np.array([1, 2, 3, 4, 5])
y = arr.view()   # view does NOT own the data
arr[0] = 42
print(arr, y)  # y is affected

print(x.base)  # None -> owns data
print(y.base)  # arr -> does not own data


# ----------------------------------------------------------
# NumPy Array Shape
# ----------------------------------------------------------
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)  # (2, 4)

arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr.shape)  # (1, 1, 1, 1, 4)


# ----------------------------------------------------------
# NumPy Array Reshape
# ----------------------------------------------------------
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)

newarr = arr.reshape(2, 3, 2)  # reshape into 3-D
print(newarr)

print(arr.reshape(2, 4).base)  # reshape returns a view

newarr = arr.reshape(3, 2, -1)  # unknown dimension using -1
print(newarr)

newarr = arr.reshape(-1)  # flattening the array
print(newarr)


# ----------------------------------------------------------
# NumPy Array Iterating
# ----------------------------------------------------------
arr = np.array([1, 2, 3])
for x in arr:
    print(x)

arr2d = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr2d:
    for y in x:
        print(y)

arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr3d):   # iterate all with nditer
    print(x)

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(x)  # iterate with different data type

for x in np.nditer(arr2d[:, ::2]):  # iterate with step
    print(x)

for idx, x in np.ndenumerate(arr):  # enumerate with index
    print(idx, x)


# ----------------------------------------------------------
# NumPy Array Join
# ----------------------------------------------------------
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)
print(arr)

arr = np.stack((arr1[0], arr2[0]), axis=0)  # stack
print(arr)

arr = np.hstack((np.array([1, 2]), np.array([3, 4])))  # stack rows
print(arr)

arr = np.vstack((np.array([1, 2]), np.array([3, 4])))  # stack columns
print(arr)

arr = np.dstack((np.array([1, 2]), np.array([3, 4])))  # stack depth-wise
print(arr)


# ----------------------------------------------------------
# NumPy Array Split
# ----------------------------------------------------------
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr)

arr2d = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
newarr = np.array_split(arr2d, 2)
print(newarr)

newarr = np.array_split(arr2d, 2, axis=1)  # split along columns
print(newarr)


# ----------------------------------------------------------
# NumPy Array Search
# ----------------------------------------------------------
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)

x = np.where(arr % 2 == 0)  # search for even
print(x)

arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7)  # find insertion index (sorted)
print(x)

x = np.searchsorted(arr, 7, side='right')
print(x)

x = np.searchsorted(arr, [2, 4, 6])  # multiple values
print(x)


# ----------------------------------------------------------
# NumPy Array Sort
# ----------------------------------------------------------
arr = np.array([3, 2, 0, 1])
print(np.sort(arr))

arr = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr))  # alphabetical

arr2d = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr2d))  # sorts each row


# ----------------------------------------------------------
# NumPy Array Filter
# ----------------------------------------------------------
arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
print(arr[x])

filter_arr = arr > 42  # creating filter directly
newarr = arr[filter_arr]
print(filter_arr, newarr)


# ==========================================================
# NUMPY RANDOM
# ==========================================================

from numpy import random

# ----------------------------------------------------------
# Random Intro
# ----------------------------------------------------------
x = random.randint(100)  # random integer 0-100
print(x)

x = random.rand()  # random float 0-1
print(x)


# ----------------------------------------------------------
# Data Distribution
# ----------------------------------------------------------
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
print(x)


# ----------------------------------------------------------
# Random Permutation
# ----------------------------------------------------------
arr = np.array([1, 2, 3, 4, 5])
print(random.shuffle(arr))  # shuffles in place
print(arr)

print(random.permutation(arr))  # returns a new shuffled array


# ----------------------------------------------------------
# Seaborn Module
# ----------------------------------------------------------
# pip install seaborn
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot([0, 1, 2, 3, 4, 5], hist=False)
plt.show()


# ----------------------------------------------------------
# Normal Distribution
# ----------------------------------------------------------
x = random.normal(loc=0, scale=1, size=(2, 3))
print(x)
sns.distplot(random.normal(size=1000), hist=False)
plt.show()


# ----------------------------------------------------------
# Binomial Distribution
# ----------------------------------------------------------
x = random.binomial(n=10, p=0.5, size=10)
print(x)
sns.distplot(random.binomial(n=10, p=0.5, size=1000), hist=True, kde=False)
plt.show()


# ----------------------------------------------------------
# Poisson Distribution
# ----------------------------------------------------------
x = random.poisson(lam=2, size=10)
print(x)
sns.distplot(random.poisson(lam=2, size=1000), kde=False)
plt.show()


# ----------------------------------------------------------
# Uniform Distribution
# ----------------------------------------------------------
x = random.uniform(size=(2, 3))
print(x)
sns.distplot(random.uniform(size=1000), hist=False)
plt.show()


# ----------------------------------------------------------
# Logistic Distribution
# ----------------------------------------------------------
x = random.logistic(loc=1, scale=2, size=(2, 3))
print(x)
sns.distplot(random.logistic(size=1000), hist=False)
plt.show()


# ----------------------------------------------------------
# Multinomial Distribution
# ----------------------------------------------------------
x = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
print(x)


# ----------------------------------------------------------
# Exponential Distribution
# ----------------------------------------------------------
x = random.exponential(scale=2, size=(2, 3))
print(x)
sns.distplot(random.exponential(size=1000), hist=False)
plt.show()


# ----------------------------------------------------------
# Chi Square Distribution
# ----------------------------------------------------------
x = random.chisquare(df=2, size=(2, 3))
print(x)
sns.distplot(random.chisquare(df=1, size=1000), hist=False)
plt.show()


# ----------------------------------------------------------
# Rayleigh Distribution
# ----------------------------------------------------------
x = random.rayleigh(scale=2, size=(2, 3))
print(x)
sns.distplot(random.rayleigh(size=1000), hist=False)
plt.show()


# ----------------------------------------------------------
# Pareto Distribution
# ----------------------------------------------------------
x = random.pareto(a=2, size=(2, 3))
print(x)
sns.distplot(random.pareto(a=2, size=1000), kde=False)
plt.show()


# ----------------------------------------------------------
# Zipf Distribution
# ----------------------------------------------------------
x = random.zipf(a=2, size=(2, 3))
print(x)

x = random.zipf(a=2, size=1000)
sns.distplot(x[x < 10], kde=False)
plt.show()


# ==========================================================
# NUMPY UFUNC
# ==========================================================

# ----------------------------------------------------------
# ufunc Intro
# ----------------------------------------------------------
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = np.add(x, y)  # ufunc example
print(z)


# ----------------------------------------------------------
# ufunc Create Function
# ----------------------------------------------------------
def myadd(x, y):
    return x + y

myadd = np.frompyfunc(myadd, 2, 1)  # (function, inputs, outputs)
print(myadd([1, 2, 3], [4, 5, 6]))
print(type(np.add))  # confirm it's a ufunc type


# ----------------------------------------------------------
# ufunc Simple Arithmetic
# ----------------------------------------------------------
arr1 = np.array([10, 11, 12])
arr2 = np.array([1, 2, 3])
print(np.add(arr1, arr2))
print(np.subtract(arr1, arr2))
print(np.multiply(arr1, arr2))
print(np.divide(arr1, arr2))
print(np.power(arr1, arr2))
print(np.mod(arr1, arr2))       # remainder
print(np.divmod(arr1, arr2))    # quotient and remainder
print(np.absolute(np.array([-1, -2, 3])))


# ----------------------------------------------------------
# ufunc Rounding Decimals
# ----------------------------------------------------------
print(np.trunc([-3.1666, 3.6667]))
print(np.fix([-3.1666, 3.6667]))
print(np.around(3.1666, 2))   # round to 2 decimals
print(np.floor([-3.1666, 3.6667]))
print(np.ceil([-3.1666, 3.6667]))


# ----------------------------------------------------------
# ufunc Logs
# ----------------------------------------------------------
arr = np.arange(1, 10)
print(np.log2(arr))
print(np.log10(arr))
print(np.log(arr))

from math import log
nplog = np.frompyfunc(log, 2, 1)  # custom log base
print(nplog(100, 15))


# ----------------------------------------------------------
# ufunc Summations
# ----------------------------------------------------------
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
print(np.sum([arr1, arr2]))
print(np.sum([arr1, arr2], axis=1))   # sum over axis
print(np.cumsum(arr1))                # cumulative sum


# ----------------------------------------------------------
# ufunc Products
# ----------------------------------------------------------
arr = np.array([1, 2, 3, 4])
print(np.prod(arr))
print(np.prod([arr1, arr2]))
print(np.prod([arr1, arr2], axis=1))
print(np.cumprod(arr))  # cumulative product


# ----------------------------------------------------------
# ufunc Differences
# ----------------------------------------------------------
arr = np.array([10, 15, 25, 5])
print(np.diff(arr))            # [5 10 -20]
print(np.diff(arr, n=2))       # discrete difference twice


# ----------------------------------------------------------
# ufunc Finding LCM
# ----------------------------------------------------------
num1, num2 = 4, 6
print(np.lcm(num1, num2))

arr = np.array([3, 6, 9])
print(np.lcm.reduce(arr))  # LCM of array elements


# ----------------------------------------------------------
# ufunc Finding GCD
# ----------------------------------------------------------
num1, num2 = 6, 9
print(np.gcd(num1, num2))

arr = np.array([20, 8, 32, 36, 16])
print(np.gcd.reduce(arr))


# ----------------------------------------------------------
# ufunc Trigonometric
# ----------------------------------------------------------
print(np.sin(np.pi / 2))
arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
print(np.sin(arr))
print(np.deg2rad(180))   # degrees to radians
print(np.rad2deg(np.pi)) # radians to degrees

x = np.arcsin(1.0)  # find angle from sine value
print(x)

base = 3
perp = 4
z = np.hypot(base, perp)  # hypotenuse
print(z)


# ----------------------------------------------------------
# ufunc Hyperbolic
# ----------------------------------------------------------
print(np.sinh(np.pi / 2))
arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
print(np.cosh(arr))
print(np.tanh(arr))
print(np.arcsinh(1.0))  # inverse hyperbolic sine


# ----------------------------------------------------------
# ufunc Set Operations
# ----------------------------------------------------------
arr1 = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
print(np.unique(arr1))  # get unique values

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])
print(np.union1d(arr1, arr2))         # union
print(np.intersect1d(arr1, arr2, assume_unique=True))  # intersection
print(np.setdiff1d(arr1, arr2, assume_unique=True))    # difference
print(np.setxor1d(arr1, arr2, assume_unique=True))     # symmetric difference


# ==========================================================
# EXTRA TOPICS (BONUS - not in original W3Schools list)
# ==========================================================

# ----------------------------------------------------------
# NumPy Linear Algebra (np.linalg)
# ----------------------------------------------------------
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

print(np.dot(a, b))         # dot product
print(a @ b)                # matrix multiplication (same as dot for 2D)
print(np.linalg.det(a))     # determinant
print(np.linalg.inv(a))     # inverse of matrix
print(np.linalg.matrix_rank(a))  # rank of matrix

eigvals, eigvecs = np.linalg.eig(a)  # eigenvalues and eigenvectors
print(eigvals)
print(eigvecs)

# solving a system of linear equations: 3x + y = 9, x + 2y = 8
coeff = np.array([[3, 1], [1, 2]])
result = np.array([9, 8])
x = np.linalg.solve(coeff, result)
print(x)


# ----------------------------------------------------------
# NumPy where() with Multiple Conditions
# ----------------------------------------------------------
arr = np.array([10, 20, 30, 40, 50])

x = np.where((arr > 15) & (arr < 45))   # AND condition
print(x)

x = np.where((arr < 15) | (arr > 45))   # OR condition
print(x)

# replace values based on condition
x = np.where(arr > 25, arr, 0)  # keep value if >25 else 0
print(x)

# nested condition (like if-elif-else)
x = np.select(
    [arr < 20, arr < 40],
    ['small', 'medium'],
    default='large'
)
print(x)


# ----------------------------------------------------------
# NumPy Broadcasting Rules
# ----------------------------------------------------------
# Broadcasting lets NumPy perform operations on arrays of
# different shapes without explicit loops.
# Rule: dimensions are compatible when they are equal,
# or one of them is 1.

a = np.array([1, 2, 3])          # shape (3,)
b = np.array([[1], [2], [3]])    # shape (3,1)
print(a + b)   # broadcasts to shape (3,3)

arr = np.array([[1, 2, 3], [4, 5, 6]])  # shape (2,3)
scalar = 10
print(arr + scalar)   # scalar is broadcast to every element

row = np.array([1, 0, 1])   # shape (3,)
print(arr + row)      # row is broadcast across each row of arr


# ----------------------------------------------------------
# NumPy Save and Load Arrays
# ----------------------------------------------------------
arr = np.array([1, 2, 3, 4, 5])

np.save('my_array.npy', arr)         # save single array (binary .npy)
loaded = np.load('my_array.npy')
print(loaded)

np.savez('my_arrays.npz', a=arr, b=arr*2)  # save multiple arrays
data = np.load('my_arrays.npz')
print(data['a'], data['b'])

np.savetxt('my_array.csv', arr, delimiter=',')  # save as text/csv
loaded_txt = np.loadtxt('my_array.csv', delimiter=',')
print(loaded_txt)


# ==========================================================
# END OF NOTES
# ==========================================================