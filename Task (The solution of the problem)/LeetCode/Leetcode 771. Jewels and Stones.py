class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        list_jewels = list(jewels)
        list_stone = list(stones)
        for item_jew in list_jewels:
            for item_stone in list_stone:
                if item_stone == item_jew:
                    count += 1
                else:
                    continue
        return count