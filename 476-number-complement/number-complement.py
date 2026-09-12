class Solution:
    def findComplement(self, num: int) -> int:
        mask = 0
        temp = num

        # Create mask of all 1s
        while temp > 0:
            mask = (mask << 1) | 1
            temp >>= 1

        # Flip the bits
        return num ^ mask