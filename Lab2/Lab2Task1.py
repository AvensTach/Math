import matplotlib.pyplot as plt
import numpy as np
import random

# ВАРІАНТ 29
VARIANТ = 29

# --- 1. Стовпчаста діаграма ---
## Кількість груп: 29 + 5 = 34
num_groups_bar = VARIANТ + 5
categories = [f'Група {i + 1}' for i in range(num_groups_bar)]

num_segments = 4
segment_names = ['Сегмент А', 'Сегмент Б', 'Сегмент В', 'Сегмент Г']
# Генеруємо випадкові дані для 34 груп, 4 сегменти
np.random.seed(42)
data_segments = np.random.randint(5, 30, size=(num_groups_bar, num_segments))

# Вибір кольорів
colors_bar = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1']

# Створення фігури та осей
plt.figure(figsize=(16, 7))
bottom = np.zeros(num_groups_bar)

for i in range(num_segments):
    plt.bar(categories, data_segments[:, i], bottom=bottom, color=colors_bar[i], label=segment_names[i])
    bottom += data_segments[:, i]

# Підписи та заголовок
plt.title(f'Стовпчаста діаграма: {num_groups_bar} Груп з 4 Сегментами (Варіант {VARIANТ})', fontsize=16)
plt.xlabel('Категорії (Групи)', fontsize=12)
plt.ylabel('Значення', fontsize=12)
plt.xticks(rotation=45, ha='right', fontsize=9)
plt.legend(title="Сегменти", loc='upper left')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

print("\n" + "=" * 80 + "\n")

# --- 2. Кругова діаграма з секторами ---
## Кількість секторів: 29 + 5 = 34
num_sectors_pie = VARIANТ + 5
sector_names = [f'Сектор {i + 1}' for i in range(num_sectors_pie)]

np.random.seed(42)
sizes = np.random.randint(10, 100, size=num_sectors_pie)


explode = [0.1 if (i + 1) % 2 == 0 else 0 for i in range(num_sectors_pie)]
explode_sum = sum(explode)  # Перевірка, чи є вийняті сектори


plt.figure(figsize=(10, 10))
wedges, texts, autotexts = plt.pie(
    sizes,
    explode=explode,
    labels=sector_names,
    autopct=lambda p: f'{p:.1f}%',
    startangle=90,
    pctdistance=0.85,
    textprops={'fontsize': 8}
)

for autotext in autotexts:
    autotext.set_color('white')  # Колір тексту відсотків
    autotext.set_weight('bold')


total_size = sum(sizes)
legend_labels = [f'{name}: {size / total_size:.1%}' for name, size in zip(sector_names, sizes)]
plt.legend(wedges, legend_labels, title="Сектори (Назва: Відсоток)", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1),
           fontsize=8)

plt.title(f'Кругова діаграма з {num_sectors_pie} Секторів(Варіант {VARIANТ})', fontsize=16)
plt.axis('equal')
plt.tight_layout()
plt.show()

print("\n" + "=" * 80 + "\n")

# --- 3. Діаграма розкиду даних ---
num_points_scatter = VARIANТ + 50

np.random.seed(42)
X = np.random.rand(num_points_scatter)
Y = np.random.rand(num_points_scatter)

# Позначення точок: Кожні 10 точок повинні мати різний стиль позначення.
markers = ['o', 's', '^', 'D', 'p', '*', 'h', 'P']  # Різні стилі маркерів

plt.figure(figsize=(10, 7))

for i, marker in enumerate(markers):
    plt.scatter(X + i * 0.2, Y + i * 0.2, marker=marker, s=100, label=f'позначення {marker}')

# Підписи та заголовок
plt.title(f'Діаграма розкиду даних: {num_points_scatter} Точок з Змінними Маркерами (Варіант {VARIANТ})', fontsize=16)
plt.xlabel('Значення по осі X', fontsize=12)
plt.ylabel('Значення по осі Y', fontsize=12)
plt.legend(title="Стилі Маркерів", loc='upper left', bbox_to_anchor=(1.01, 1), fontsize=10)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
