# graph = {
#     1: [2, 3],
#     2: [1, 4],
#     3: [1, 5],
#     4: [2],
#     5: [3]
# }
# start = 1
#
# Пример выходных данных
# [1, 2, 4, 3, 5]  # Возможен и другой порядок, зависящий от реализации DFS
def f(graph, start, visit=None):
    if visit is None:
        visit = []
    visit.append(start)

    for i in graph[start]:
        if i not in visit:
            f(graph, i, visit)

    return visit

start = 5
graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 5],
    4: [2],
    5: [3]
}


print(f(graph,start))