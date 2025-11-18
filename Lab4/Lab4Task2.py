import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
plt.switch_backend('TkAgg')

# Налаштування
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.set_title("Завдання 2: Перетин двох циліндрів (Варіант 29)")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_box_aspect([1, 1, 1]) # Робимо осі пропорційними

# Створення Циліндра 1 (x^2 + z^2 = 9)
# Рухається вздовж осі Y
u = np.linspace(0, 2 * np.pi, 50) # Кут
v = np.linspace(-7, 7, 20)       # Висота/довжина вздовж Y
U, V = np.meshgrid(u, v)

X1 = 3 * np.cos(U)
Y1 = V
Z1 = 3 * np.sin(U)
ax.plot_surface(X1, Y1, Z1, alpha=0.5, color='blue', rstride=1, cstride=1)

# Створення Циліндра 2 (x^2 + y^2 = 16)
# Рухається вздовж осі Z
# u (кут) можна використати той самий
v = np.linspace(-7, 7, 20) # Висота/довжина вздовж Z
U, V = np.meshgrid(u, v)

X2 = 4 * np.cos(U)
Y2 = 4 * np.sin(U)
Z2 = V
ax.plot_surface(X2, Y2, Z2, alpha=0.5, color='red', rstride=1, cstride=1)

# Встановлюємо фіксовані межі для стабільного обертання
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.set_zlim([-7, 7])


# Функція анімації (обертання камери)
def animate(frame):
    # Обертаємо Cцену, змінюючи кут 'azim'
    # 'elev' = 30 (кут огляду зверху)
    # 'azim' = frame (кут обертання)
    ax.view_init(elev=30, azim=4*frame)
    return fig,

anim = animation.FuncAnimation(fig, animate, frames=360,
                               interval=50, blit=False)

plt.show()