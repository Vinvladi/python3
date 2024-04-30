class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output_list = []
        d = 0
        for item in nums:
            d += item
            output_list.append(d)
        return output_list