# Реализовать алгоритм Кана для топологической сортировки
# Пример с пошаговой работой алгоритма
# Граф: A → B → C
#       A → D

graph = {"A" : ["B", "D"],
        "B" : ["C"],
        "C" : [],
        "D" : []}

# Шаги:
# 1. Начальные вершины без входящих рёбер: [A]
# 2. Обрабатываем A → результат [A], обновляем степени B(1→0), D(1→0)
# 3. Вершины для обработки: [B, D]
# 4. Обрабатываем B → результат [A,B], обновляем степень C(1→0)
# 5. Обрабатываем D → результат [A,B,D]
# 6. Обрабатываем C → результат [A,B,D,C]
# 7. Все вершины обработаны → сортировка завершена
def f(graph):
    stepen = {}
    for n in graph:
        stepen[n] = 0

    for n in graph:
        for neighbor in graph[n]:
            stepen[neighbor] += 1

    queue = []
    for n in stepen:
        if stepen[n] == 0:
            queue.append(n)

    res = []

    while queue:
        cur = queue.pop(0)
        res.append(cur)

        for neighbor in graph[cur]:
            stepen[neighbor] -= 1

            if stepen[neighbor] == 0:
                queue.append(neighbor)

    if len(res) != len(graph):
        return "топологическая сортировка невозможна"

    return res

print("Исходный граф:", graph)
result = f(graph)
print("\nФинальный результат топологической сортировки:", result)