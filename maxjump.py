class Solution:
    def maxJump(self, nums) -> bool:
        dp = [9999999]*(len(nums))
        dp[0]=0
        for i in range(len(nums)-1):
            if i+nums[i]+1 >= len(nums):
                for j in range(i+1, len(nums)):
                    dp[j] = min(dp[j], dp[i]+1)
            else:
                for j in range(i+1, i+nums[i]+1):
                    dp[j] = min(dp[j], dp[i]+1)
                    # print(dp, i, j)

        if dp[len(nums)-1] == 9999999:
            return False
        return True

    def canJump(self, nums) -> bool:

        lastZeroIdx = -1
        for i in range(len(nums)-2, -1,-1):
            if lastZeroIdx == -1 and nums[i] == 0:
                lastZeroIdx = i
            if lastZeroIdx > -1 and (i + nums[i]) > lastZeroIdx:
                lastZeroIdx = -1
        if lastZeroIdx > -1:
            return False
        return True


[3,4,1,1,2,4]

prevfar = 3
