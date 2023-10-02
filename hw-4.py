# Корреляция
# ● Контекст
# Корреляция - статистическая мера, используемая для оценки
# связи между двумя случайными величинами.
# ● Ваша задача
# Написать скрипт для расчета корреляции Пирсона между
# двумя случайными величинами (двумя массивами). Можете
# использовать любую парадигму, но рекомендую использовать
# функциональную, т.к. в этом примере она значительно
# упростит вам жизнь

import numpy as np


def pearson_correlation(x, y):
    # Проверяем, что оба массива имеют одинаковую длину
    if len(x) != len(y):
        raise ValueError("Массивы должны иметь одинаковую длину")

    # Вычисляем средние значения для x и y
    mean_x = np.mean(x)
    mean_y = np.mean(y)

    # Вычисляем числитель и знаменатель для корреляции Пирсона
    numerator = np.sum((x - mean_x) * (y - mean_y))
    denominator_x = np.sqrt(np.sum((x - mean_x) ** 2))
    denominator_y = np.sqrt(np.sum((y - mean_y) ** 2))

    # Вычисляем корреляцию Пирсона
    correlation = numerator / (denominator_x * denominator_y)

    return correlation


# Пример использования:
x = [2, 2, 3, 4, 5]
y = [22, 3, 4, 5, 6]

correlation_coefficient = pearson_correlation(x, y)
print(f"Корреляция Пирсона между x и y: {correlation_coefficient}")
