# Даны N городов и M дорог между ними. Дороги двусторонние (граф неориентированный). 
# Известно, что города разделены на группы (острова), 
# между которыми дорог нет. То есть граф состоит из нескольких компонент связности (островов). 
# Необходимо ответить на следующие вопросы:
# 
# 1. Есть ли путь между двумя заданными городами (вершинами)?
# 2. Сколько всего островов (компонент связности) в графе?
# 3.Перечислить, какие города принадлежат каждому острову.
# 
# Входные данные:
# Первая строка: N (количество городов) и M (количество дорог).
# Следующие M строк: пары чисел u и v, обозначающие дорогу между городами u и v.
# Затем вводится два числа: start и end — номера городов, между которыми нужно проверить наличие пути.
# 
# Выходные данные:
# Ответ на вопрос, есть ли путь между start и end ("YES" или "NO").
# Количество островов (компонент связности) в графе.
# Список городов для каждого острова (в порядке возрастания номеров островов).

# Пример 1:
# 5 3
# 1 2
# 2 3
# 4 5
# 1 4
# 
# Ожидаемый вывод:
# 
# NO
# 2
# 1: [1, 2, 3]
# 2: [4, 5]

# Пример 2:
# 6 4
# 1 2
# 3 4
# 5 6
# 2 3
# 3 5
# 
# Ожидаемый вывод:
# 
# YES
# 1
# 1: [1, 2, 3, 4, 5, 6]

# Пример 3:
# 7 0
# 1 2
# 
# Ожидаемый вывод:
# 
# NO
# 7
# 1: [1]
# 2: [2]
# 3: [3]
# 4: [4]
# 5: [5]
# 6: [6]
# 7: [7]
start1 = 1
end1 = 4
a1 = [1,2,3,4,5]
graph1 = {1: [2],
          2: [3,1],
          3: [2],
          4: [5],
          5: [4],}
if graph1[start1] == end1:
    print("YES")
else:
    print("NO")
def f(graph, start, visit=None):
    if visit is None:
        visit = []
    visit.append(start)

    for i in graph[start]:
        if i not in visit:
            f(graph, i, visit)

    return visit
result_1 = f(graph1,start1)
result_12 = f(graph1,4)
print(2)
print("1" , result_1)
print("2" , result_12)
start3 =1
end3 = 2
graph3 = {1: [1],
2: [2],
3: [3],
4: [4],
5: [5],
6: [6],
7: [7]}
if graph3[start3] == end3:
    print("YES")
else:
    print("NO")
s=0
for i in graph3:
    if len(graph3[i]) == 1 and :
        s +=1
print(s)
if s ==7:
    print(graph3)


