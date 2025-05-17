from collections import deque

def bfs(graph, start, finish):
    queue = deque([start])
    visited = {start: None}  # Словарь для отслеживания предков

    while queue:
        current = queue.popleft()

        if current == finish:
            # Восстанавливаем путь от finish до start
            path = []
            while current is not None:
                path.append(current)
                current = visited[current]
            return path[::-1]  # Возвращаем путь в правильном порядке

        for neighbor in graph[current]:
            if neighbor not in visited:  # Если сосед еще не посещен
                visited[neighbor] = current  # Запоминаем предка
                queue.append(neighbor)  # Добавляем соседа в очередь

    return None  # Если путь не найден

# Пример использования
city_map = {
    'Home': ['Park', 'School', 'Mail'],
    'Park': ['Home', 'Museum', 'Cafe'],
    'School': ['Home', 'Library', 'Mail'],
    'Mail': ['Home', 'School', 'Hospital'],
    'Library': ['School', 'Hospital'],
    'Hospital': ['Library', 'Mail', 'Office'],
    'Cafe': ['Park', 'Theater', 'Office'],
    'Museum': ['Park', 'Shop'],
    'Shop': ['Museum', 'Theater'],
    'Theater': ['Shop', 'Cafe'],
    'Office': ['Cafe', 'Hospital']
}
start = "Home"
finish = "Theater"

path = bfs(city_map, start, finish)

if path:
    print("Путь от", start, "до", finish, ":", path)
else:
    print("Путь не найден.")