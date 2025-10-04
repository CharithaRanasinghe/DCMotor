import numpy as np
import matplotlib.pyplot as plt

La = 0.04
Ra = 20.0
KE = 0.5
KT = 0.5
J  = 0.001
D  = 0.2

dt = 0.0001
N = 5000

A = np.array([
    [1.0,       0.0,      dt,     0.0],
    [0.0,       1.0,      0.0,    dt],
    [-Ra/La,   -KE/La,    0.0,    0.0],
    [ KT/J,    -D/J,      0.0,    0.0]
])

B = np.array([0.0, 0.0, 1.0/La, 0.0]).reshape((4,1))
C = np.array([0.0, 0.0, 0.0, -1.0/J]).reshape((4,1))

V = 12.0    # Applied Voltage in Volts
TL = 0.05   # Load Torque Acting on the Armature

X = np.zeros((4,1))
i_hist = np.zeros(N)
w_hist = np.zeros(N)
t = np.arange(0, N*dt, dt)

for k in range(N):
    i_hist[k] = X[0,0]
    w_hist[k] = X[1,0]
    X = A @ X + B*V + C*TL

plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.plot(t, i_hist); plt.xlabel('t (s)'); plt.ylabel('i (A)'); plt.grid(True)
plt.subplot(1,2,2)
plt.plot(t, w_hist); plt.xlabel('t (s)'); plt.ylabel('omega (rad/s)'); plt.grid(True)
plt.tight_layout()
plt.show()
