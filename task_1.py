import random

scores = [random.randint(1, 100) for _ in range(random.randint(7, 10))]

print("Исходные баллы:", scores)

min_score = min(scores)
max_score = max(scores)

print(f"Удаляем минимум ({min_score}) и максимум ({max_score}).")

scores.remove(min_score)
scores.remove(max_score)

print("Оставшиеся баллы:", scores)

average = sum(scores) / len(scores)

print("Средний рейтинг:", average)