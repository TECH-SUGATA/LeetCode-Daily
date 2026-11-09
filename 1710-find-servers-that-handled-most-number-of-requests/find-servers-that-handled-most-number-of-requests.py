from sortedcontainers import SortedList

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        available = SortedList(range(k))
        busy = []
        count = [0] * k

        for i, (a, l) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= a:
                _, server = heapq.heappop(busy)
                available.add(server)

            if not available:
                continue

            idx = available.bisect_left(i % k)

            if idx == len(available):
                idx = 0

            server = available.pop(idx)

            count[server] += 1
            heapq.heappush(busy, (a + l, server))

        maximum = max(count)

        return [i for i in range(k) if count[i] == maximum]