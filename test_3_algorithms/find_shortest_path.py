from random import randint
import networkx
from colorama import init, Back


init(autoreset=True)
# море, суша
SEA, LAND = 0, 1


def generate_map(rows, columns, start, finish, land_percentage=0.3):
    """Генерация карты
    :param rows: параметр поля M
    :param columns: параметр поля N
    :param start: начальная точка
    :param finish: конечная точка
    :param land_percentage: процент суши
    """
    # создаем матрицу состоящую полностью из моря
    sea_map = [[SEA for _ in range(columns)] for _ in range(rows)]

    # считаем количество клеток с сушей и распределяем по карте моря в произвольном порядке
    # начальную и конечную точки по умолчанию считаем морем
    land_cells = round(rows * columns * land_percentage)
    while land_cells > 0:
        row = randint(0, rows - 1)
        col = randint(0, columns - 1)
        if (row, col) not in [start, finish] and sea_map[row][col] != LAND:
            sea_map[row][col] = LAND
            land_cells -= 1
    return sea_map


def draw_shortest_path(sea_map, start, finish):
    """Поиск кратчайшего пути
    :param sea_map: карта
    :param start: начальная точка
    :param finish: конечная точка
    """
    rows = len(sea_map)
    columns = len(sea_map[0])

    # делаем из карты граф
    map_graph = networkx.Graph()
    # добавляем узлы
    for row in range(rows):
        for col in range(columns):
            # если точка море - добавляем узел
            if sea_map[row][col] == SEA:
                map_graph.add_node((row, col))

    # добавляем ребра
    # направления поиска (вверх, вниз, влево, вправо)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for row in range(rows):
        for col in range(columns):
            if sea_map[row][col] == SEA:
                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc
                    if 0 <= new_row < rows and 0 <= new_col < columns and sea_map[new_row][new_col] == SEA:
                        map_graph.add_edge((row, col), (new_row, new_col))

    shortest_path = []
    try:
        shortest_path = networkx.shortest_path(map_graph, start, finish)
    except networkx.NetworkXNoPath:
        print('Между указанными точками нет пути по морю на данной сгенерированной карте при заданных условиях')
    for row in range(rows):
        for col in range(columns):
            coord = (row, col)
            i = sea_map[row][col]
            if coord == start:
                sea_map[row][col] = f'{Back.RED}A'
            elif coord == finish:
                sea_map[row][col] = f'{Back.RED}B'
            elif coord in shortest_path:
                sea_map[row][col] = f'{Back.LIGHTBLUE_EX}{i}'
            else:
                sea_map[row][col] = f'{Back.GREEN if i else Back.BLUE}{i}'
        print(' '.join(sea_map[row]))


def start_prog(rows, columns, start, end):
    if any(type(value) is not int or value <= 0 for value in [rows, columns, *start, *end]):
        raise TypeError('Размеры поля и координаты точек должны быть указаны в виде натуральных чисел')
    if not ((0 <= start[0] < rows) or (0 <= start[1] < columns)):
        raise ValueError('Координаты начальной точки находятся за пределами поля')
    if not ((0 <= end[0] < rows) or (0 <= end[1] < columns)):
        raise ValueError('Координаты конечной точки находятся за пределами поля')

    # смещаем координаты под индексы матрицы
    start = (start[0] - 1, start[1] - 1)
    end = (end[0] - 1, end[1] - 1)
    print(f'Где-то в Японии: старт {start}-> финиш {end}')
    # генерируем карту
    automap = generate_map(m, n, start, end)
    # ищем кратчайший путь
    draw_shortest_path(automap, start, end)


# пользовательские данные
m = 20
n = 30
start_point = (randint(1, m), randint(1, n))
end_point = (randint(1, m), randint(1, n))

start_prog(m, n, start_point, end_point)
