
def second_char (str2):
    extr_str=[]
    for ir in str2:

        i=ir[1]
        print(i)
        if (i == "a" or i=="e" or i== "i"  or i== "u" or i =="o" ):
         extr_str.append(i)

    return extr_str;


input_str=input("enter the string: ").split(",")
e=second_char(input_str)
print(e)