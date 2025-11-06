import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

plt.switch_backend('TkAgg')

# --- Налаштування полярної системи координат ---
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.set_title("Завдання 3: r = 6 * cos(5*Phi) (Варіант 29)", va='bottom')
ax.set_rmax(6.5)
ax.set_rticks([2, 4, 6])
ax.grid(True)

# --- Ініціалізуємо тільки лінію ---
line, = ax.plot([], [], lw=2, color='blue')

# --- Параметри анімації ---
# Збільшимо кількість кадрів, щоб промальовка була плавною
draw_frames = 250

# --- *** НОВИЙ СПОСІБ ГЕНЕРАЦІЇ БАЗОВОЇ ФОРМИ *** ---

points_per_petal = 100  # Кількість точок на одну пелюстку

# 1. Створюємо 'шаблон' для однієї пелюстки (де r завжди >= 0)
# Кут для однієї пелюстки (від -pi/10 до pi/10, тобто -18° до +18°)
phi_petal_template = np.linspace(-np.pi / 10, np.pi / 10, points_per_petal)
# 'r' для однієї пелюстки (від 0 до 6 і назад до 0)
r_petal_template = 6 * np.cos(5 * phi_petal_template)

# 2. Додаємо точку (0,0) в кінці кожної пелюстки, щоб "підняти ручку"
# (Ми використовуємо phi=0, r=0 як "точку повернення")
phi_petal_template = np.concatenate([phi_petal_template, [0]])
r_petal_template = np.concatenate([r_petal_template, [0]])

# 3. Створюємо повний шлях, копіюючи шаблон 5 разів з обертанням
phi_base = np.array([])
r_base = np.array([])

for i in range(5):
    # Додаємо кут зсуву для кожної нової пелюстки (0°, 72°, 144°, ...)
    angle_shift = i * (2 * np.pi / 5)

    phi_base = np.concatenate([phi_base, phi_petal_template + angle_shift])
    r_base = np.concatenate([r_base, r_petal_template])

# 4. Отримуємо загальну кількість точок у нашому новому шляху
total_segments = len(phi_base)

# --- Кінець нового способу генерації ---

# Конвертуємо наш *новий* (правильний) шлях в декартові координати
# Це потрібно для ФАЗИ 2 (Обертання)
x_base = r_base * np.cos(phi_base)
y_base = r_base * np.sin(phi_base)


# --- Функція анімації ---
def animate(frame):
    if frame <= draw_frames:
        # --- ФАЗА 1: Промальовка ---
        # Ця логіка тепер працює правильно, оскільки phi_base/r_base
        # описують безперервний шлях малювання
        current_segment_count = int((frame / draw_frames) * total_segments)

        current_phi = phi_base[:current_segment_count]
        current_r = r_base[:current_segment_count]

        line.set_data(current_phi, current_r)

    else:
        # --- ФАЗА 2: Обертання ---
        # Ця частина залишається незмінною. Вона бере повну фігуру
        # (x_base, y_base) і обертає її
        rotation_angle = (frame - draw_frames) * 0.03

        x_new = x_base * np.cos(rotation_angle) - y_base * np.sin(rotation_angle)
        y_new = x_base * np.sin(rotation_angle) + y_base * np.cos(rotation_angle)

        r_new = np.sqrt(x_new ** 2 + y_new ** 2)
        phi_new = np.arctan2(y_new, x_new)
        sort_indices = np.argsort(phi_new)

        line.set_data(phi_new[sort_indices], r_new[sort_indices])

    return line,


# --- Створення та запуск анімації ---
anim = animation.FuncAnimation(fig, animate, frames=None,
                               interval=30, blit=True)

plt.show()