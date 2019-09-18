import numpy as np
import matplotlib.pyplot as plt
import math

len = 10000
time = np.linspace(0.000,0.050,len)
amplitude = (15.570562)*abs(np.sin(time*100*math.pi))
#amplitude = time * time
plt.plot(time, amplitude)
plt.title('output of bridge rectifier')
plt.xlabel('$time(sec)$')
plt.ylabel('$X(t) in volts$')
plt.grid(linestyle='--')
plt.plot(0.005,15.570562,'o')
plt.show()
