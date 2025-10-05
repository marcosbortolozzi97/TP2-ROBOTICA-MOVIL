
import re
import numpy as np
import matplotlib.pyplot as plt

# Cargar el log con parser manual
tsec, tnsec, x, y, yaw, v, w = [], [], [], [], [], [], []

with open("log_Circulo_carga.txt") as f:
    next(f)
    for line in f:
        # Extraer todos los números (positivos o negativos, con decimales)
        nums = re.findall(r"[-+]?\d*\.\d+|\d+", line)
        if len(nums) >= 6:  # asegurarse de que haya al menos 6 números
            tsec.append(float(nums[0]))       # timestamp (segundos)
            tnsec.append(float(nums[1]))       # timestamp (segundos)
            x.append(float(nums[2]))
            y.append(float(nums[3]))
            yaw.append(float(nums[4]))
            v.append(float(nums[5]))
            w.append(float(nums[6]))

# Convertir a arrays de numpy
tsec = np.array(tsec)
tnsec = np.array(tnsec)
x = np.array(x)
y = np.array(y)
yaw = np.array(yaw)
v = np.array(v)
w = np.array(w)

# ---- Gráfico 1: camino x-y ----
plt.figure()
plt.plot(x, y, 'b-')
plt.xlabel("x [m]")
plt.ylabel("y [m]")
plt.title("Camino seguido por el robot")
plt.axis('equal')
plt.grid(True)

# ---- Gráfico 2: trayectoria ----
plt.figure()
plt.plot(tsec, x, label="x(t)")
plt.plot(tsec, y, label="y(t)")
plt.plot(tsec, yaw, label="θ(t)")
plt.xlabel("Tiempo [s]")
plt.ylabel("Pose")
plt.title("Trayectoria en el tiempo")
plt.legend()
plt.grid(True)

plt.show()
