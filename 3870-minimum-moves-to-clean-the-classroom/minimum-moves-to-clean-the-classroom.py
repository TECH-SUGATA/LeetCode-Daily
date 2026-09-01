from collections import deque

class Solution:
    def minMoves(self, classroom, energy):
        m = len(classroom)
        n = len(classroom[0])

        start = None
        litter_id = {}
        k = 0

        # Find S and all L positions
        for r in range(m):
            for c in range(n):
                cell = classroom[r][c]

                if cell == 'S':
                    start = (r, c)

                elif cell == 'L':
                    litter_id[(r, c)] = k
                    k += 1

        # No litter
        if k == 0:
            return 0

        target = (1 << k) - 1

        # visited[r][c] is a dictionary:
        # mask -> maximum energy seen at this state
        visited = [[{} for _ in range(n)] for _ in range(m)]

        sr, sc = start
        visited[sr][sc][0] = energy

        # r, c, remaining_energy, mask
        q = deque([(sr, sc, energy, 0)])

        moves = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            for _ in range(len(q)):
                r, c, e, mask = q.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if nr < 0 or nr >= m or nc < 0 or nc >= n:
                        continue

                    if classroom[nr][nc] == 'X':
                        continue

                    # Cannot move without energy
                    if e == 0:
                        continue

                    ne = e - 1
                    nmask = mask

                    # Collect litter
                    if (nr, nc) in litter_id:
                        nmask |= 1 << litter_id[(nr, nc)]

                    # Reset energy
                    if classroom[nr][nc] == 'R':
                        ne = energy

                    # All litter collected
                    if nmask == target:
                        return moves + 1

                    # Dominance check:
                    # If this state was already reached with >= energy,
                    # this state is useless.
                    old_energy = visited[nr][nc].get(nmask, -1)

                    if ne <= old_energy:
                        continue

                    visited[nr][nc][nmask] = ne
                    q.append((nr, nc, ne, nmask))

            moves += 1

        return -1