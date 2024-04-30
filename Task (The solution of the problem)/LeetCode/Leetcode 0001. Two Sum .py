class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        k = []
        for item_1 in range(0,len(nums)-1,1):
            for item_2 in range(item_1 + 1,len(nums),1):
                d = nums[item_1]
                f = nums[item_2]
                if target == d + f:
                    k.append(item_1)
                    k.append(item_2)
                    break
            if len(k) == 2:
                break
        return k
# untime: 4226 ms (Beats 13.83%) / Memory: 15 MB (Beats 58.61%)