

s= input("Enter the string")
sub= input("Enter the substring ")

if sub in s:
    s = s.replace(sub, "")
    print(s)