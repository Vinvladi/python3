def plastic_balance(list):
   for item in list:
       for k in range(0,len(item)//2,1):
           


"""   for k in range(0, math.floor(len([list])/2), 1):
        if list[0] + list[-1] != sum(list[1:-1]):
            list.pop(0) and list.pop(-1)
            if len(list) == 0:
                return []
        elif list[0] + list[-1] == sum(list[1:-1]):
            return print("Yes")

        
Ex1:

        [1, 2, 3, 4, 5] == > 1 + 5 != 2 + 3 + 4 == > [2, 3, 4] == > 2 + 4 != 3 == [3] == > 3 + 3 != 0 == > []

        note: (3 + 3)
        because
        3 is first
        side and last
        side...( != 0) because
        sum
        of
        list
        without
        sides = 0

        Ex2:

        [0, 104, 3, 101, 0, 111] == > 0 + 111 != 104 + 3 + 101 + 0 == > [104, 3, 101, 0] == > 104 + 0 = 3 + 101 == > [
            104, 3, 101, 0]

        Ex3:

        [1, -1] == > 1 - 1 = 0 == > [1, -1]
"""