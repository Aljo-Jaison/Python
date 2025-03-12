

s=input("Enter the string : ")
for i in s:
    if i==" ":
        s=s.replace(" ","*")

s=s+'$'

print(s)