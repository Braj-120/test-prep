#User function Template for python3
class Solution:
    def minOperations(self, s1, s2):
		# code here
        n = len(s1)
        m = len(s2)
        
        arr = [None] * (n+1)
        for i in range(n+1):
            arr[i] = [0]*(m+1)
        for k in range(1, m+1):
            arr[0][k] = k
        for k in range(1, n+1):
            arr[k][0] = k
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                print(i, j)
                if s1[i-1] == s2[j-1]:
                    arr[i][j] = arr[i-1][j-1]
                    
                else:
                    arr[i][j] = min(arr[i][j-1], arr[i-1][j]) + 1
        
        return arr[n][m]
                    
                    
                    
#{ 
 # Driver Code Starts
#Initial Template for Python 3

# if __name__ == '__main__':
# 	T=int(input())
# 	for i in range(T):
# 		s1,s2 = input().split()
# 		ob = Solution()
# 		ans = ob.minOperations(s1,s2)
# 		print(ans)
# # } Driver Code Ends

ob = Solution()
ans = ob.minOperations("heap", "pea")
print(ans)