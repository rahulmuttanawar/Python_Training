
def first_last_char (str2):
    extr_str=[]
    for i in str2:
         extr_str.append(i[0])
         extr_str.append(i[-1])


    return extr_str;


input_str=input("enter the string: ").split(",")
e=first_last_char(input_str)
print(e)