def isHappy(n):
    num=n
    while num >9 and num!=1:
        res=0
        for i in str(num):
            res=res+(int(i)*int(i))
        num=res
    if num!=1:
        return False
    return True

print(isHappy(9))

        