import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
plt.switch_backend('TkAgg')
# --- Налаштування фігури та осей ---
fig, ax = plt.subplots()
# Встановлюємо межі, від яких крива буде "відбиватися"
xlims = [-2, 4]
ylims = [-1, 3]
ax.set_xlim(xlims[0], xlims[1])
ax.set_ylim(ylims[0], ylims[1])
ax.set_title("Завдання 1: Анімація 2D-кривої (Варіант 29)")
ax.set_xlabel("X")
ax.set_ylabel("Y")

# --- Визначення базової кривої (Варіант 29б) ---
# t повинно бути в діапазоні [0, 1]
t = np.linspace(0, 1, 400)
x_base = np.arccos(np.sqrt(1 - t**2))
y_base = np.arcsin(np.sqrt(1 - t))

# Ініціалізуємо лінію, яку будемо анімувати
line, = ax.plot([], [], lw=2)

# --- Глобальні змінні для анімації ---
offset_x = 0.0
offset_y = 0.0
direction_x = 1  # 1 = вправо, -1 = вліво
direction_y = 1  # 1 = вгору, -1 = вниз
speed_x = 0.05
speed_y = 0.02
colors = ['blue', 'red', 'green']

# --- Функція ініціалізації анімації ---
def init():
    line.set_data([], [])
    return line,

# --- Функція анімації (викликається для кожного кадру) ---
def animate(frame):
    global offset_x, direction_x, offset_y, direction_y

    # --- Логіка руху по X (вліво-вправо) ---
    current_x_min = x_base.min() + offset_x
    current_x_max = x_base.max() + offset_x

    # Перевірка на зіткнення з межами X
    if (current_x_max >= xlims[1] and direction_x == 1) or \
       (current_x_min <= xlims[0] and direction_x == -1):
        direction_x *= -1  # Змінити напрямок

    # --- Логіка руху по Y (вгору-вниз) ---
    current_y_min = y_base.min() + offset_y
    current_y_max = y_base.max() + offset_y

    # Перевірка на зіткнення з межами Y
    if (current_y_max >= ylims[1] and direction_y == 1) or \
       (current_y_min <= ylims[0] and direction_y == -1):
        direction_y *= -1  # Змінити напрямок

    # Оновлення зсувів
    offset_x += direction_x * speed_x
    offset_y += direction_y * speed_y

    # Оновлення даних лінії
    line.set_data(x_base + offset_x, y_base + offset_y)

    # --- Логіка зміни кольору ---
    # Змінюємо колір кожні 40 кадрів
    color_index = (frame // 40) % len(colors)
    line.set_color(colors[color_index])

    return line,

# --- Створення та запуск анімації ---
# blit=True для плавності
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=None, interval=20, blit=True)

plt.grid(True)
plt.show()