


s= input("Enter the string : ")
result=[]
for i in range(len(s)):
    if i % 2 == 0:
        result.append(s[i])

print("".join(result))