class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counts = [0] * n
        indexes = list(range(n))

        def merge_sort(left, right):
            if left >= right:
                return

            mid = (left + right) // 2

            merge_sort(left, mid)
            merge_sort(mid + 1, right)

            temp = []
            i, j = left, mid + 1
            smaller = 0

            while i <= mid and j <= right:
                if nums[indexes[j]] < nums[indexes[i]]:
                    temp.append(indexes[j])
                    smaller += 1
                    j += 1
                else:
                    counts[indexes[i]] += smaller
                    temp.append(indexes[i])
                    i += 1

            while i <= mid:
                counts[indexes[i]] += smaller
                temp.append(indexes[i])
                i += 1

            while j <= right:
                temp.append(indexes[j])
                j += 1

            indexes[left:right + 1] = temp

        merge_sort(0, n - 1)
        return counts