class Solution:
    def minSumOfLengths(self, arr, target):
        n = len(arr)

        # best[i] = shortest target-sum subarray
        # completely inside arr[0:i]
        best = [float('inf')] * (n + 1)

        left = 0
        curr_sum = 0

        answer = float('inf')
        shortest = float('inf')

        for right in range(n):
            curr_sum += arr[right]

            # Shrink window if sum becomes too large
            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1

            # Found a subarray with sum = target
            if curr_sum == target:
                length = right - left + 1

                # Combine with the best previous subarray
                if best[left] != float('inf'):
                    answer = min(answer, best[left] + length)

                # Update shortest subarray seen so far
                shortest = min(shortest, length)

            # Best subarray completely before/right up to current index
            best[right + 1] = shortest

        return -1 if answer == float('inf') else answer