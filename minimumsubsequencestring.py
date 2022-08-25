class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        cDict = {}
        
        for i in t:
            if i in cDict:
                cDict[i] +=1
            else:
                cDict[i]=1
        
        i,j = 0,0
        count = len(cDict.keys())
        
        minLength = 9999999
        start=0
        end=len(s)-1
        
        for i in (range(len(s))):
            if s[i] in cDict:
                cDict[s[i]] -=1
                
                if cDict[s[i]] == 0:
                    count -= 1
                    
            while count == 0:
                if minLength > (i-j)+1:
                    start = j
                    end = i
                    minLength = (end-start)+1
                    # print(s[start:end+1],j,i,minLength)
                # print(cDict)
                if s[j] in cDict:
                    cDict[s[j]] += 1
                    if cDict[s[j]] > 0:
                        count += 1
                j+=1
        if minLength == 9999999:
            return ""
        return s[start:end+1]
        
        