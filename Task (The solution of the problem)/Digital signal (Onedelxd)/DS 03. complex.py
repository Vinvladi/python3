import math

d = int(input(("Введите кол-во операций: ")))
base = - math.pi / 4
base_int = "π/4"
list_base = [2.4, 2, 1.76, 1.616, 1.5296, 1.4777, 1.4466, 1.4279]
basic_complex = complex(0, 1)
vivod = complex(0, 0)
vivod_r = complex(0, 0)
elem_list = []  # лист элементов
elem_list_cos_sin = []
for index_i in range(0, d + 1, 1):
    for index_j in range(0, d + 1, 1):
        vivod = list_base[index_j] * (
                math.cos(base * index_i * index_j) + basic_complex * math.sin(base * index_i * index_j)) + vivod
        vivod_r = list_base[index_j] * (
                math.cos(base * index_i * index_j) + basic_complex * math.sin(base * index_i * index_j))
        l1 = f"x({index_j})*e^-i*{base_int})*{index_i}*{index_j}"
        elem_list.append(l1)
        l2 = f"x({index_j})*cos(-{base_int} * {index_i} * {index_j}) + i*sin(-{base_int} * {index_i} * {index_j})"
        elem_list_cos_sin.append(l2)
        print(vivod_r)
    print(elem_list)
    print(elem_list_cos_sin)
    print(f"Для значения {index_i} он равен {vivod}")
    vivod = complex(0, 0)
    elem_list = []
    elem_list_cos_sin = []
