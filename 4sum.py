class Solution:
    def fourSum(self, nums, target):
        n = len(nums)
        nums.sort()
        # print(nums)
        out = []
        for i in range(n-1):
            if i>0 and nums[i-1] == nums[i]:
                continue
            for j in range(i+1, n-1):
                if j>i+1 and nums[j-1] == nums[j]:
                    continue
                l = j+1
                r=n-1
                # print(i,j,l,r)
                while l<r:
                    sumof = nums[i] + nums[j] + nums[l] + nums[r]
                    # print(sumof)
                    if sumof > target:
                        r -=1
                    elif sumof < target:
                        l+=1
                    else:
                        out.append([nums[i] ,nums[j] , nums[l] , nums[r]])
                        # print([nums[i] ,nums[j] , nums[l] , nums[r]])
                        l+=1
                        while nums[l] == nums[l-1] and l<r:
                            l+=1
                        
        return out
                    