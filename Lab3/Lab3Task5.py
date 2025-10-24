import matplotlib.pyplot as plt
import numpy as np

plt.switch_backend('TkAgg')

plt.switch_backend('TkAgg')
# Налаштування фігури та 3D-осей
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

# Кількість стовпчиків згідно з варіантом (29 + 4)
n_bars = 33

# Генерація випадкових даних для першої діаграми
x1 = np.random.rand(n_bars) * 10 # координати x
y1 = np.random.rand(n_bars) * 10 # координати y
z1 = np.zeros(n_bars)           # координати z дорівнюють 0
dx1 = np.ones(n_bars) * 0.5     # ширина стовпчиків
dy1 = np.ones(n_bars) * 0.5     # глибина стовпчиків
dz1 = np.random.rand(n_bars) * 5 # висота стовпчиків

ax.bar3d(x1, y1, z1, dx1, dy1, dz1, color='c', alpha=0.7, label='Діаграма 1 (z=0)')

# Генерація випадкових даних для другої діаграми
x2 = np.random.rand(n_bars) * 10 # координати x
y2 = np.random.rand(n_bars) * 10 # координати y
z2 = np.ones(n_bars) * 2           # координати z дорівнюють 2
dx2 = np.ones(n_bars) * 0.5     # ширина стовпчиків
dy2 = np.ones(n_bars) * 0.5     # глибина стовпчиків
dz2 = np.random.rand(n_bars) * 5 # висота стовпчиків

ax.bar3d(x2, y2, z2, dx2, dy2, dz2, color='m', alpha=0.7, label='Діаграма 2 (z=2)')

# Генерація даних для третьої діаграми
x3 = np.random.rand(n_bars) * 10

y3 = np.linspace(0.05, 10, n_bars)
z3 = np.zeros(n_bars) # Починаючи з основи z=0

for i in range(n_bars):
    z3[i] = round(np.random.ranf(), 2)
    print(z3[i], end=' ')
    
dx3 = np.ones(n_bars) * 0.5
dy3 = np.ones(n_bars) * 0.2 # Невелика глибина
dz3 = np.random.rand(n_bars) * 8 # Висота стовпчиків

# Побудова третьої діаграми
ax.bar3d(x3, y3, z3, dx3, dy3, dz3, color='y', alpha=0.7, label='Діаграма 3 (y змінюється)')

# --- Налаштування графіка ---
ax.set_xlabel('Вісь X')
ax.set_ylabel('Вісь Y')
ax.set_zlabel('Вісь Z')
ax.set_title('Три просторові стовпчикові діаграми')
ax.legend()

# Збереження графіка
plt.show()