ir=list(input("enter the string : ").split(","))

print(type(ir))
for i in ir:
    if(i.__contains__("and")):
        print(i)
    else:
        continue