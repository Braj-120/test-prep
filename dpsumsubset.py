#User function Template for python3

from re import sub


class Solution:
    dps = None
    def isSubsetSum (self, N, arr, sum):
        # code here 
        m = sum+1
        n = len(arr)+1
        dp = [[False for _ in range(m)] for _ in range(n)]
        for i in range(n):
            dp[i][0] = True
        # print(dp)
        for i in range(1,n):
            for j in range(1,m):
                # print(i,j)
                dp[i][j] = dp[i-1][j]
                
                if arr[i-1] == j:
                    dp[i][j] = True
                
                if arr[i-1] < j:
                    dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i][j]
        self.dps = dp
        return dp[n-1][m-1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

# if __name__ == '__main__': 
#     t = int (input ())
#     for _ in range (t):
#         N = int(input())
#         arr = input().split()
#         for itr in range(N):
#             arr[itr] = int(arr[itr])
#         sum = int(input())

#         ob = Solution()
#         if ob.isSubsetSum(N,arr,sum)==True:
#             print(1)
#         else :
#             print(0)
            
        

# # } Driver Code Ends

ob = Solution()
s = ob.isSubsetSum(6, [3, 34, 4, 12, 5, 2], 9)
print(s)
