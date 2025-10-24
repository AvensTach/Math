import numpy as np
import matplotlib.pyplot as plt

plt.switch_backend('TkAgg')

def plot_surface():
    # Створення сітки координат X та Y
    # Визначаємо діапазон для X та Y
    x = np.linspace(-3, 3, 100)
    y = np.linspace(-6, 6, 100)
    X, Y = np.meshgrid(x, y)

    # Обчислення координати Z за рівнянням поверхні:
    # 4z = 4x^2 - y^2 + 4y + 4
    # z = x^2 - 0.25*y^2 + y + 1
    Z = X**2 - 0.25 * Y**2 + Y + 1

    # Ініціалізація 3D-графіка
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    surface = ax.plot_surface(X, Y, Z,
                              cmap='viridis',
                              rstride=5,
                              cstride=5,
                              alpha=0.8,
                              linewidth=0,
                              antialiased=False)

    # Додавання колірної шкали
    fig.colorbar(surface, shrink=0.5, aspect=5, label='Значення Z')

    # Налаштування осей та заголовка
    ax.set_xlabel('Вісь X')
    ax.set_ylabel('Вісь Y')
    ax.set_zlabel('Вісь Z')
    ax.set_title(r'Гіперболічний параболоїд: $4x^2 - y^2 + 4y - 4z + 4 = 0$')

    # Відображення графіка
    plt.show()

# Виконання функції
plot_surface()