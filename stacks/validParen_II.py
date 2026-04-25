s="leet(code))))"
s1=""
s2=""
stack=[]
count=0

for i in range(len(s)):
    
    if s[i]=="(":
        stack.append("(")
        count+=1
        s1=s1+s[i]
    elif s[i]==")":a
        if stack:
            stack.pop()
            count-=1
            s1=s1+s[i]
    else:
        s1=s1+s[i]

print(s1)
print(count)
for j in range(len(s1)):
    if s1[j]=="(":
        count-=1
        if count<0:
            s2=s2+"("
    else:
        s2=s2+s1[j]
print(s2)
        

    
        
