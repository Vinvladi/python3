# Циклический сдвиг в массиве
# Это операция преобразования данных в массиве
#  влево                                                                вправо
# 0 1 2 3 4                                                             0 1 2 3 4
# 1 2 3 4 0                                                             4 0 1 2 3    
# tmp [0] -->                                                           
# Само движение происходит слева на право пошагово               
# более подробно в тетрадке на странице 16-17 
# Для ВЛЕВО:
# tmp = A[0]
# for k in range(N-1): # то есть k переберет 0,1,2,3 индексы
#   A[k] = A[k+1]
# A[N-1] = tmp
# Для ВПРАВО:
# tmp = A[N-1]
# for k in range (N-2,-1,-1):
#   A[k+1] = A[k]
# A[0] = tmp
 