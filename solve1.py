import numpy as np
import matplotlib.pyplot as plt

dx = .001
x = np.arange(0,1+dx,dx)
nx = x.shape[0]
y = np.arange(0,1+dx,dx)

xv, yv = np.meshgrid(x,y)
Tx = np.zeros(xv.shape)
Ty = np.zeros(xv.shape)

xmin = 0.45
xmax = 0.55

# Define Tx, Ty:
for ii in range(0,nx):
    for jj in range(0,nx):
        if xv[ii,jj] > xmin and xv[ii,jj] < xmax and yv[ii,jj] > xmin and yv[ii,jj] < xmax:
            Tx[ii,jj] = 1




