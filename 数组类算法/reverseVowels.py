class Solution:
    def reverseVowels(self, s: str) -> str:
        i,j=0,len(s)-1
        vowel=['a','e','i','o','u']
        slist=list(s)
        while i<j:
            if slist[i].lower() not in vowel:
                i+=1
                continue
            if slist[j].lower() not in vowel:
                j-=1
                continue
            slist[i],slist[j]= slist[j],slist[i]
            i+=1
            j-=1
        s=''.join(slist)    
        return s
sl=Solution() 
print(sl.reverseVowels("aA"))