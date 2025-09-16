tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

stack=[]



for i in range(len(tokens)):
    if tokens[i] not in "+/-*":
        stack.append(int(tokens[i]))
    else:
        op1=stack.pop()
        op2=stack.pop()
        if tokens[i]=="+":
            stack.append(op2+op1)

        elif tokens[i]=="-":
            stack.append(op2-op1)

        elif tokens[i]=="*":
            stack.append(op2*op1)
        else:
            stack.append(int(op2/op1))
print(stack[0])