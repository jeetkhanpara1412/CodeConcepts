import numpy as np
import scipy

# ==========================================================
# SCIPY TUTORIAL - FULL NOTES
# ==========================================================


# ----------------------------------------------------------
# SciPy Home
# ----------------------------------------------------------
# SciPy is a scientific computation library built on top of NumPy.
# It provides more utility functions for optimization, stats,
# signal processing, linear algebra, and more.

# ----------------------------------------------------------
# SciPy Intro
# ----------------------------------------------------------
# SciPy stands for "Scientific Python". It is open source and
# used for high-level scientific/mathematical computations.
print(scipy.__version__)


# ----------------------------------------------------------
# SciPy Getting Started
# ----------------------------------------------------------
# SciPy is built on NumPy arrays. Most SciPy modules need to
# be imported separately, e.g.: from scipy import constants
from scipy import constants
print(constants.pi)   # example of using a SciPy sub-module


# ----------------------------------------------------------
# SciPy Constants
# ----------------------------------------------------------
from scipy import constants

print(constants.liter)          # 0.001 (1 liter in cubic meters)
print(constants.golden)          # golden ratio
print(constants.speed_of_light)   # speed of light
print(constants.gravitational_constant)

# unit categories
print(constants.gram)     # mass units
print(constants.minute)    # time units
print(constants.inch)       # length units
print(constants.bar)         # pressure units
print(constants.kmh)          # speed units
print(constants.zero_Celsius) # temperature units (in Kelvin)

# find all constant category functions
print(dir(constants))


# ---- Unit Categories in scipy.constants ----

# Binary
print(constants.kibi)   # 1024
print(constants.mebi)    # 1024^2
print(constants.gibi)     # 1024^3
print(constants.tebi)      # 1024^4
print(constants.pebi)       # 1024^5
print(constants.exbi)        # 1024^6
print(constants.zebi)         # 1024^7
print(constants.yobi)          # 1024^8

# Mass
print(constants.gram)         # 0.001 kg
print(constants.metric_ton)    # 1000 kg
print(constants.grain)          # grain in kg
print(constants.lb, constants.pound)   # pound in kg
print(constants.oz, constants.ounce)    # ounce in kg
print(constants.stone)                   # stone in kg
print(constants.long_ton)                 # long ton in kg
print(constants.short_ton)                 # short ton in kg
print(constants.troy_ounce)                 # troy ounce in kg
print(constants.troy_pound)                  # troy pound in kg
print(constants.carat)                        # carat in kg
print(constants.atomic_mass, constants.m_u, constants.u)  # atomic mass unit

# Angle
print(constants.degree)        # degree in radians
print(constants.arcmin, constants.arcminute)  # arcminute in radians
print(constants.arcsec, constants.arcsecond)   # arcsecond in radians

# Time
print(constants.minute)     # 60 seconds
print(constants.hour)        # 3600 seconds
print(constants.day)          # seconds in a day
print(constants.week)          # seconds in a week
print(constants.year)           # seconds in a year
print(constants.julian_year)     # seconds in a julian year

# Length
print(constants.inch)             # inch in meters
print(constants.foot)              # foot in meters
print(constants.yard)               # yard in meters
print(constants.mile)                # mile in meters
print(constants.mil)                  # mil in meters
print(constants.pt, constants.point)   # point in meters
print(constants.survey_foot)             # US survey foot
print(constants.survey_mile)              # US survey mile
print(constants.nautical_mile)             # nautical mile in meters
print(constants.fermi)                      # fermi in meters
print(constants.angstrom)                    # angstrom in meters
print(constants.micron)                       # micron in meters
print(constants.au, constants.astronomical_unit)  # astronomical unit
print(constants.light_year)                        # light year in meters
print(constants.parsec)                              # parsec in meters

# Pressure
print(constants.atm, constants.atmosphere)  # standard atmosphere in pascals
print(constants.bar)                          # bar in pascals
print(constants.torr, constants.mmHg)          # torr / mmHg in pascals
print(constants.psi)                            # psi in pascals

# Volume
print(constants.liter, constants.litre)   # liter in cubic meters
print(constants.gallon, constants.gallon_US)  # US gallon in cubic meters
print(constants.gallon_imp)                     # imperial gallon in cubic meters
print(constants.fluid_ounce, constants.fluid_ounce_US)  # US fluid ounce
print(constants.fluid_ounce_imp)                          # imperial fluid ounce
print(constants.barrel, constants.bbl)                      # oil barrel in cubic meters

# Speed
print(constants.kmh)              # km/h in m/s
print(constants.mph)               # mph in m/s
print(constants.mach, constants.speed_of_sound)  # speed of sound in m/s
print(constants.knot)                              # knot in m/s

# Temperature
print(constants.zero_Celsius)        # 0 Celsius in Kelvin
print(constants.degree_Fahrenheit)     # 1 degree Fahrenheit in Kelvin (scale factor)

# Energy
print(constants.eV, constants.electron_volt)   # electron volt in joules
print(constants.calorie, constants.calorie_th)    # thermochemical calorie in joules
print(constants.calorie_IT)                         # IT calorie in joules
print(constants.erg)                                  # erg in joules
print(constants.Btu, constants.Btu_IT)                  # British thermal unit in joules
print(constants.Btu_th)                                   # thermochemical BTU in joules
print(constants.ton_TNT)                                    # ton of TNT in joules

# Power
print(constants.hp, constants.horsepower)   # horsepower in watts

# Force
print(constants.dyn, constants.dyne)          # dyne in newtons
print(constants.lbf, constants.pound_force)    # pound-force in newtons
print(constants.kgf, constants.kilogram_force)  # kilogram-force in newtons


# ----------------------------------------------------------
# SciPy Optimizers
# ----------------------------------------------------------
from scipy.optimize import root, minimize

def eqn(x):
    return x + np.cos(x)   # find root of x + cos(x) = 0

myroot = root(eqn, 0)
print(myroot.x)      # the root
print(myroot.fun)     # value of function at root

def eqn2(x):
    return x**2 + x + 2   # find minimum of this function

mymin = minimize(eqn2, 0, method='BFGS')
print(mymin)
print(mymin.x)   # the x value at minimum


# ----------------------------------------------------------
# SciPy Sparse Data
# ----------------------------------------------------------
from scipy.sparse import csr_matrix, csc_matrix

arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
print(csr_matrix(arr))   # compressed sparse row matrix

sparse_arr = csr_matrix(arr)
print(sparse_arr.data)        # non-zero data values
print(sparse_arr.count_nonzero())  # number of non-zero elements

sparse_arr.eliminate_zeros()   # remove explicit zero entries
sparse_arr.sum_duplicates()     # combine duplicate entries

print(csr_matrix(arr).tocsc())   # convert from csr to csc


# ----------------------------------------------------------
# SciPy Graphs
# ----------------------------------------------------------
from scipy.sparse.csgraph import connected_components, dijkstra, floyd_warshall
from scipy.sparse import csr_matrix

graph_arr = np.array([
    [0, 1, 2],
    [1, 0, 0],
    [2, 0, 0]
])
newarr = csr_matrix(graph_arr)

print(connected_components(newarr))   # find connected components

print(dijkstra(newarr, return_predecessors=True, indices=0))  # shortest path

print(floyd_warshall(newarr, return_predecessors=True))   # all-pairs shortest path

from scipy.sparse.csgraph import bellman_ford
bf_arr = np.array([
    [0, -1, 2],
    [1, 0, 0],
    [2, 0, 0]
])
newarr2 = csr_matrix(bf_arr)
print(bellman_ford(newarr2, return_predecessors=True, indices=0))

from scipy.sparse.csgraph import depth_first_order, breadth_first_order
dfs_arr = np.array([
    [0, 1, 0, 1],
    [1, 1, 1, 1],
    [2, 1, 1, 0],
    [0, 1, 0, 1]
])
newarr3 = csr_matrix(dfs_arr)
print(depth_first_order(newarr3, 1))
print(breadth_first_order(newarr3, 1))


# ----------------------------------------------------------
# SciPy Spatial Data
# ----------------------------------------------------------
from scipy.spatial import KDTree, ConvexHull, Delaunay
from scipy.spatial.distance import euclidean, cityblock, cosine, hamming

points = [(1, -1), (2, 3), (-2, 3), (2, -3)]
kdtree = KDTree(points)
res = kdtree.query((1, 1))   # find nearest neighbor
print(res)

hull_points = np.array([[0, 0], [10, 0], [10, 10], [0, 10]])
hull = ConvexHull(hull_points)
print(hull.vertices)    # points that make up the convex hull

tri_points = np.array([[0, 0], [1, 0], [0, 1], [1, 1]])
tri = Delaunay(tri_points)
print(tri.simplices)   # triangulation

p1 = (1, 0)
p2 = (10, 2)
print(euclidean(p1, p2))    # euclidean distance
print(cityblock(p1, p2))     # manhattan distance
print(cosine(p1, p2))         # cosine distance
print(hamming((True, False, True), (False, True, True)))  # hamming distance


# ----------------------------------------------------------
# SciPy Matlab Arrays
# ----------------------------------------------------------
from scipy import io

mat_arr = np.arange(10)
io.savemat('arr.mat', {"vec": mat_arr})   # export array to a .mat file

mydata = io.loadmat('arr.mat')   # import array from a .mat file
print(mydata['vec'])

# use squeeze_me=True to remove extra dimensions on load
mydata2 = io.loadmat('arr.mat', squeeze_me=True)
print(mydata2['vec'])


# ----------------------------------------------------------
# SciPy Interpolation
# ----------------------------------------------------------
from scipy.interpolate import interp1d, UnivariateSpline, Rbf

xs = np.arange(10)
ys = 2 * xs + 1
interp_func = interp1d(xs, ys)   # 1D interpolation
print(interp_func(2.5))

xs2 = np.arange(10)
ys2 = xs2**2 + np.sin(xs2) + 1
spline = UnivariateSpline(xs2, ys2)   # spline interpolation
print(spline(2.5))

xs3 = np.arange(10)
ys3 = xs3**2 + np.sin(xs3) + 1
rbf_func = Rbf(xs3, ys3)   # radial basis function interpolation
print(rbf_func(2.5))


# ----------------------------------------------------------
# SciPy Significance Tests
# ----------------------------------------------------------
from scipy.stats import ttest_ind, kstest, describe, normaltest, chi2_contingency

v1 = np.random.normal(size=100)
v2 = np.random.normal(size=100)

res_t = ttest_ind(v1, v2)   # T-Test: compare means of two samples
print(res_t)
print(res_t.pvalue)

res_ks = kstest(v1, 'norm')   # Kolmogorov-Smirnov Test: fit to distribution
print(res_ks)

res_desc = describe(v1)   # descriptive statistics
print(res_desc)

res_norm = normaltest(v1)   # test whether sample differs from normal distribution
print(res_norm)

contingency_table = np.array([[10, 20], [30, 40]])
res_chi2 = chi2_contingency(contingency_table)   # Chi-Square Test
print(res_chi2)


# ==========================================================
# EXTRA TOPICS (BONUS - beyond the official tutorial)
# ==========================================================

# ----------------------------------------------------------
# SciPy Integration
# ----------------------------------------------------------
from scipy.integrate import quad, dblquad, odeint, solve_ivp

# quad() - single definite integral
result, error = quad(lambda x: x**2, 0, 1)   # integral of x^2 from 0 to 1
print(result, error)

# dblquad() - double integral
result2, error2 = dblquad(lambda y, x: x * y, 0, 1, 0, 1)  # integral over x and y from 0 to 1
print(result2, error2)

# odeint() - solve ordinary differential equations (legacy API)
def model(y, t):
    return -0.5 * y   # dy/dt = -0.5y

t = np.linspace(0, 10, 100)
y0 = 5
sol = odeint(model, y0, t)
print(sol[:5])

# solve_ivp() - modern API for solving initial value problems
def model2(t, y):
    return -0.5 * y

sol2 = solve_ivp(model2, [0, 10], [5], t_eval=t)
print(sol2.y[0][:5])


# ----------------------------------------------------------
# SciPy Linear Algebra
# ----------------------------------------------------------
from scipy import linalg

la_arr = np.array([[1, 2], [3, 4]])

print(linalg.det(la_arr))          # determinant
print(linalg.inv(la_arr))           # inverse

b = np.array([5, 6])
print(linalg.solve(la_arr, b))       # solve system of linear equations Ax = b

eigvals, eigvecs = linalg.eig(la_arr)  # eigenvalues and eigenvectors
print(eigvals)
print(eigvecs)

U, s, Vh = linalg.svd(la_arr)   # singular value decomposition
print(U, s, Vh)

P, L, Uu = linalg.lu(la_arr)   # LU decomposition
print(P, L, Uu)

print(linalg.norm(la_arr))   # matrix/vector norm


# ----------------------------------------------------------
# SciPy Signal Processing
# ----------------------------------------------------------
from scipy import signal

sig = np.array([1, 2, 1, 0, -1, -2, -1, 0, 1, 2, 1])

b, a = signal.butter(3, 0.2)             # design a Butterworth filter
filtered = signal.filtfilt(b, a, sig)     # apply the filter (zero-phase)
print(filtered)

conv_result = signal.convolve([1, 2, 3], [0, 1, 0.5])   # convolution
print(conv_result)

peaks, _ = signal.find_peaks(sig)   # find local peaks in a signal
print(peaks)

detrended = signal.detrend(sig)   # remove linear trend from data
print(detrended)


# ----------------------------------------------------------
# SciPy Fourier Transforms
# ----------------------------------------------------------
from scipy.fft import fft, ifft, fftfreq

t_fft = np.linspace(0, 1, 400, endpoint=False)
signal_fft = np.sin(2 * np.pi * 50 * t_fft) + 0.5 * np.sin(2 * np.pi * 80 * t_fft)

yf = fft(signal_fft)               # forward Fourier transform
xf = fftfreq(len(t_fft), 1 / 400)   # frequency bins
print(yf[:5])
print(xf[:5])

y_reconstructed = ifft(yf)   # inverse Fourier transform
print(y_reconstructed[:5])


# ----------------------------------------------------------
# SciPy Image Processing (scipy.ndimage)
# ----------------------------------------------------------
from scipy import ndimage

img = np.zeros((10, 10))
img[3:7, 3:7] = 1   # a simple square "image"

blurred = ndimage.gaussian_filter(img, sigma=1)   # Gaussian blur
print(blurred)

rotated = ndimage.rotate(img, angle=45, reshape=False)  # rotate image
print(rotated)

shifted = ndimage.shift(img, shift=(1, 1))   # shift image
print(shifted)

edges = ndimage.sobel(img)   # edge detection
print(edges)


# ----------------------------------------------------------
# SciPy Clustering
# ----------------------------------------------------------
from scipy.cluster.vq import kmeans, vq, whiten
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster

cluster_data = np.array([[1, 1], [1.5, 2], [3, 4], [5, 7], [3.5, 5], [4.5, 5], [3.5, 4.5]])

whitened = whiten(cluster_data)          # normalize data before clustering
centroids, distortion = kmeans(whitened, 2)   # k-means clustering (2 clusters)
print(centroids, distortion)

cluster_ids, _ = vq(whitened, centroids)   # assign points to clusters
print(cluster_ids)

Z = linkage(cluster_data, method='ward')   # hierarchical clustering
print(Z)

clusters = fcluster(Z, t=2, criterion='maxclust')   # form flat clusters
print(clusters)


# ----------------------------------------------------------
# SciPy Statistical Distributions
# ----------------------------------------------------------
from scipy.stats import norm, binom, poisson, uniform, expon

# Normal distribution
print(norm.pdf(0))            # probability density at x=0
print(norm.cdf(1.96))          # cumulative probability up to x=1.96
print(norm.rvs(size=5))         # random samples

# Binomial distribution
print(binom.pmf(3, n=10, p=0.5))   # probability of exactly 3 successes
print(binom.rvs(n=10, p=0.5, size=5))

# Poisson distribution
print(poisson.pmf(2, mu=3))    # probability of exactly 2 events
print(poisson.rvs(mu=3, size=5))

# Uniform distribution
print(uniform.rvs(size=5))

# Exponential distribution
print(expon.rvs(scale=2, size=5))

# fitting a distribution to data
data = norm.rvs(loc=5, scale=2, size=1000)
mu_fit, std_fit = norm.fit(data)
print(mu_fit, std_fit)


# ==========================================================
# END OF NOTES
# ==========================================================