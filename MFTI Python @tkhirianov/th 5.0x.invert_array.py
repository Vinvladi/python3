def invert_array(A:list, N:int):
# Обращение массива (поворот задом-наперед)
# в рамках индексов от 0 до N-1
    # for k in range(N):  
    #    A[k] = A [N-1-k] - в данном случае элементы будут перетирать друг друга и будут к примеру при первом тесте [5,4,3,4,5] в тетрадке наглядный график
    # for k in range(N):   
    #    A[k], A[N-1-k] = A[N-1-k], A[k] - в данном случае также fail в тетрадке разбор на стр 16
    for k in range(N//2):   # до середины с целым делением, так как элемент середины не будет менятся
        A[k], A[N-1-k] = A[N-1-k], A[k]

def test_invert_array():
    A1 = [1, 2, 3, 4, 5]
    print(A1)
    invert_array (A1, 5)
    print(A1)
    if A1 == [5, 4, 3, 2, 1]:
        print("#test1 - ok")
    else:
        print("#test1 - fail")
    
    A2 = [-1, -2, -3, -4, -5, 0, 87]
    print(A2)
    invert_array (A2, 7)
    print(A2)
    if A2 == [87, 0, -5, -4, -3, -2, -1]:
        print("#test2 - ok")
    else:
        print("#test2 - fail")

test_invert_array () #запуск данной функции