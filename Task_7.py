import random
import matplotlib.pyplot as plt

def simulate_dice_rolls(num_rolls=100000):
    sum_counts = {i: 0 for i in range(2, 13)}

    # Симуляція кидання кубиків
    for _ in range(num_rolls):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        dice_sum = dice1 + dice2
        sum_counts[dice_sum] += 1

    probabilities = {key: (value / num_rolls) * 100 for key, value in sum_counts.items()}
    return probabilities, sum_counts

num_rolls = 100000
simulated_probabilities, simulated_counts = simulate_dice_rolls(num_rolls)

theoretical_probabilities = {
    2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89,
    7: 16.67, 8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78
}


print("Сума\tІмовірність (симуляція)\tІмовірність (теоретична)")
for sum_value in range(2, 13):
    print(f"{sum_value}\t{simulated_probabilities[sum_value]:.2f}%\t\t\t{theoretical_probabilities[sum_value]}%")

# Побудова графіку
sums = list(simulated_probabilities.keys())
simulated_values = list(simulated_probabilities.values())
theoretical_values = list(theoretical_probabilities.values())

plt.figure(figsize=(10, 6))
plt.bar(sums, simulated_values, alpha=0.6, label="Симуляція (Монте-Карло)", color='skyblue')
plt.plot(sums, theoretical_values, marker='o', color='red', label="Теоретичні значення", linestyle='dashed')
plt.xlabel("Сума")
plt.ylabel("Імовірність (%)")
plt.title("Імовірність отримання сум чисел на двох кубиках")
plt.legend()
plt.grid(True)
plt.show()
