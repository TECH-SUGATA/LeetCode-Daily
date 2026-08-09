import random

class Solution:
    def __init__(self, nums):
        self.nums = nums

    def pick(self, target):
        return random.choice([i for i, x in enumerate(self.nums) if x == target])