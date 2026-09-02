class Solution:
    def findRestaurant(self, list1, list2):
        index = {word: i for i, word in enumerate(list1)}

        min_sum = float('inf')
        ans = []

        for j, word in enumerate(list2):
            if word in index:
                total = index[word] + j

                if total < min_sum:
                    min_sum = total
                    ans = [word]
                elif total == min_sum:
                    ans.append(word)

        return ans