s="racecar"

resLen=0
res=""
for i in range(len(s)):
#odd length

    l,r=i,i
    while l>=0 and r<len(s) and s[l]==s[r]:
        if (r-l+1)>resLen:
            resLen=r-l+1
            res=s[l:r+1]
        l-=1
        r+=1

#even length
    l,r=i,i+1
    while l>=0 and r<len(s) and s[l]==s[r]:
        if(r-l+1)>resLen:
            resLen=r-l+1
        l-=1
        r+=1

print(res)

