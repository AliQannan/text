from numpy import *
fname = '1.txt'
dtype1 = dtype([('gender', '|S1'), ('height', 'f8')])
a = loadtxt(fname, dtype=dtype1, skiprows=9, usecols=(1,3))
print(a)
