class Solution:  # 1502. Can Make Arithmetic Progression From Sequence

    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        d = arr[1] - arr[0]
        for item in range(0, len(arr)-1):
            if d == arr[item+1] -arr[item]:
                continue
            else:
                return False
                break
        return True
