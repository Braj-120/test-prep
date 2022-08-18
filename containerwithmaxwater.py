class Solution:
    def maxArea(self, height) -> int:
        l=0
        r=len(height) - 1
        maxi = 0
        while l<r:
            maxi = max(maxi, min(height[l], height[r]) * (r-l))
            if height[l] > height[r]:
                r-=1
            else:
                l+=1
        return maxi
                       