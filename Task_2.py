import matplotlib.pyplot as plt
import numpy as np

def draw_pythagoras_tree(x, y, angle, length, depth, ax):
    if depth == 0:
        return

    x_end = x + length * np.cos(angle)
    y_end = y + length * np.sin(angle)

    ax.plot([x, x_end], [y, y_end], color="brown", linewidth=1)

    new_length = length * np.sqrt(2) / 2
    left_angle = angle + np.pi / 4
    right_angle = angle - np.pi / 4
    draw_pythagoras_tree(x_end, y_end, left_angle, new_length, depth - 1, ax)
    draw_pythagoras_tree(x_end, y_end, right_angle, new_length, depth - 1, ax)

# Основна програма для візуалізації
def visualize_pythagoras_tree(depth):
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_aspect('equal')
    ax.axis('off')

    draw_pythagoras_tree(0, 0, np.pi / 2, 1, depth, ax)
    plt.show()

# Запит рівня рекурсії у користувача
try:
    depth = int(input("Введіть рівень рекурсії для дерева Піфагора: "))
    if depth < 1:
        print("Рівень рекурсії повинен бути більшим або рівним 1.")
    else:
        visualize_pythagoras_tree(depth)
except ValueError:
    print("Будь ласка, введіть ціле число.")
