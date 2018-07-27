import numpy as np
import matplotlib.pyplot as plt

"""Plot the VCO open loop data"""
plt.subplot(221)
x = 10**np.linspace(0.0, 8.0, 50)
x_closed = 10**np.linspace(0.0, 4.5, 10)

plt.semilogx(x, -24*np.log10(x)+11, label="open loop")
plt.semilogx(x_closed, -85+0*x_closed, label="closed loop")

plt.semilogx(1e3, -60, ".")
plt.semilogx(2*1e3, -68, ".")
plt.semilogx(20*1e6, -158, ".")
plt.semilogx(80*1e3, -110, ".")
plt.semilogx(5*1e3, -80, ".")
plt.semilogx(1e4, -85, ".")
plt.semilogx(1*1e6, -132, ".")
plt.semilogx(1000, -55, ".")

plt.legend()
plt.title('VCO open loop data carrier 5GHz (individual points are from datasheet)')
plt.grid(True)

# Axis limits
plt.xlim(1000, 100*1e6)
plt.ylim(-170, -50)

# Label axes
plt.xlabel("Freq offset from carrier (Hz)")
plt.ylabel("dBc/Hz")

"""Plot the estimated radians^2/Hz noise"""
plt.subplot(222)
# Use same x values as before by default. Or can change them later
plt.loglog(x, 2*10**(.1*(-24*np.log10(x)+11)))
plt.loglog(x_closed, 2*10**(.1*(-85+0*x_closed)), label="closed loop")
plt.xlim(xmin=10)
plt.xlabel("Frequency offset from carrier (Hz)")

plt.title('VCO Rad^2/Hz open loop carrier 5GHz')
plt.grid(True)


"""Plot the estimated flux/root Hz noise"""
dphase_dflux = 300.  # dphase/dflux multiplied by phi0
plt.subplot(223)
# Use same x values as before by default. Or can change them later
# calculate with dflux/dphase * sqrt(radians squared per hertz)
plt.loglog(x, (1/dphase_dflux)*np.sqrt(2*10**(.1*(-24*np.log10(x)+11))), label=
           "open loop")
plt.loglog(x_closed, (1/dphase_dflux)*np.sqrt(2*10**(.1*(-85+0*x_closed))), label=
           "closed loop")

plt.xlabel("Flux frequency (Hz)")
plt.legend()
plt.title("Flux noise phi0/sqrtHz")

"""Plot the Bluhm data for comparison (will later replace with ours)"""
csv_filename = "Default_Dataset.csv"
csv_data = np.genfromtxt(csv_filename, delimiter=',')
for i in range(np.shape(csv_data)[0]):
    plt.scatter(csv_data[i, 0], csv_data[i, 1])

plt.xlabel("Flux frequency (Hz)")
plt.title("Data from Bluhm")
plt.xlim(10, 1e7)
plt.ylim(ymin=1e-8)

plt.grid(True)
plt.show()
