class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
       
        # code here
        dp = [[0 for _ in range(W+1)] for _ in range(n+1)]
                    

        for i in range(1,n+1):
            for j in range(1,W+1):
                dp[i][j] = dp[i-1][j]
                if j >= wt[i-1]:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-wt[i-1]]+val[i-1])
        #     print(dp[i])
        # print(dp[n][W])
        return dp[n][W]

    def unboundedKnapsack(self, N, W, val, wt):
        dp = [0]*(W+1)
        for w in range(1, W+1):
            for i in range(N):
                if wt[i] <= w:
                    print(w, wt[i], w-wt[i])
                    dp[w] = max(dp[w], val[i]+dp[w-wt[i]])
            print(dp[w])
        print(dp[W])
        return dp[W]



# Solution().knapSack(8, [1, 4, 5, 7], [1, 3, 4, 5], 4)
Solution().unboundedKnapsack(4, 8, [1, 4, 5, 7], [1, 3, 4, 5])