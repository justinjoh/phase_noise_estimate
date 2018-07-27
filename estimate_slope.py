
"""Use this to estimate dphase/dflux"""
import numpy as np
import matplotlib.pyplot as plt
import math

real_gamma_filename = "Default_Dataset_real_gamma.csv"
imaginary_gamma_filename = "Default_Dataset_imaginary_gamma.csv"
real_gamma = np.genfromtxt(real_gamma_filename, delimiter=",")
imaginary_gamma = np.genfromtxt(imaginary_gamma_filename, delimiter=",")

real_shape = np.shape(real_gamma)
imaginary_shape = np.shape(imaginary_gamma)

max_length = min(real_shape[0], imaginary_shape[0])
phase_arr = np.empty((max_length, 2))
for i in range(max_length):     # linearly interpolate
    x_val = real_gamma[i, 0]

    pos = 0     # index position
    while pos <= np.max(real_gamma[0]) and pos <= max_length-1:
            if imaginary_gamma[pos, 0] < x_val:
                pos += 1
    real_val = real_gamma[i, 1]
    imaginary_val = imaginary_gamma[pos, 1]
    phase = math.atan(imaginary_val/real_val)
    phase_arr[i, 0] = x_val
    phase_arr[i, 1] = phase

plt.subplot(111)
plt.scatter(phase_arr[:, 0], phase_arr[:, 1])

plt.xlabel('flux (phi0)')
plt.ylabel('Phase shift (radians)')
plt.show()
