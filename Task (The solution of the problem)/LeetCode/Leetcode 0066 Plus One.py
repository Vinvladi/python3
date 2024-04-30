class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits_new = int(''.join(map(str, digits)))
        digits_new += 1
        digits = [int(digits) for digits in str(digits_new)]
        return digits