class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        shuffle_list = [0] * len(s)
        count = 0
        for index in indices:
            shuffle_list.insert(index, s[count])
            shuffle_list.pop(index+1)
            count += 1
        shuffle_list = ''.join(shuffle_list)
        return shuffle_list

# Создаем экземпляр класса Solution
solution = Solution()

# Вызываем функцию restoreString и передаем ей входные данные
result = solution.restoreString("vinaoknch", [1, 0, 3, 2, 5, 4, 6, 7, 8])

# Выводим результат
print(result)  # выведет "leetcode"
