s = "A man, a plan, a canal: Panama"

s=s.lower()

s="".join([c for c in s if c.isalnum()])

l,r = 0,len(s)-1
while r>l:
    if s[l]!=s[r]:
        print("False")
        break
    l+=1
    r-=1

print("True")
    