class Solution:
    def isValidMove(self, KnightPos, move, N):
        if KnightPos[0] + move[0] > 0 and KnightPos[1] + move[1] > 0 and KnightPos[0] + move[0] < N+1 and KnightPos[1]+move[1] < N+1:
            return True
        return False

    def minStepToReachTarget(self, KnightPos, TargetPos, N):
		#Code here
        moves = [[1, 2], [1, -2], [-1, 2], [-1, -2],
                 [2, 1], [2, -1], [-2, 1], [-2, -1]]
        queue = []
        visited = [[False]*N for _ in range(N)]
        currpos = KnightPos
        currpos.append(0)
        queue.append(currpos)
        visited[currpos[0] - 1][currpos[1] - 1] = True
        while len(queue) > 0:
            currpos = queue.pop(0)
            dist = currpos[2]
            for move in moves:
                nextpos = [currpos[0] + move[0], currpos[1] + move[1], dist+1]
                if nextpos[0] == TargetPos[0] and nextpos[1] == TargetPos[1]:
                    return nextpos[2]
                if self.isValidMove(currpos, move, N) and visited[nextpos[0]-1][nextpos[1]-1] == False:
                    visited[nextpos[0]-1][nextpos[1]-1] = True
                    queue.append(nextpos)
        return -1

print(Solution().minStepToReachTarget([7,7],[1,5], 8))