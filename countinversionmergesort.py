class Solution:
    #User function Template for python3
    
    # arr[]: Input Array
    # N : Size of the Array arr[]
    #Function to count inversions in the array.
    def inversionCount(self, arr, n):
        # Your Code Here
        l = 0
        r = n - 1
        temparr = [0]*n
        return self.divide(arr, l, r, temparr)
    
    def divide(self, arr, l, r, temp):
        invcount = 0

        if l<r:
            mid = (l+r) // 2

            invcount += self.divide(arr, l, mid, temp)
            invcount += self.divide(arr, mid+1, r, temp)
            invcount += self.merge(arr, l, mid, r, temp)
        return invcount
    
    def merge(self, arr, l, mid, r, temparr):
        i = l
        j = mid+1
        invcount = 0
        k = l
        while i<=mid and j<=r:
            if arr[i]>arr[j]:
                temparr[k] = arr[j]
                invcount += (mid-i + 1)
                k+=1
                j+=1
            else:
                temparr[k]=arr[i]
                k+=1
                i+=1
            
        while i<=mid:
            temparr[k] = arr[i]
            k+=1
            i+=1
        while j<=r:
            temparr[k] = arr[j]
            k+=1
            j+=1
        for loop_var in range(l, r + 1):
            arr[loop_var] = temparr[loop_var]
        return invcount


o = Solution().inversionCount([2, 4, 1, 3, 5], 5)
print(o)