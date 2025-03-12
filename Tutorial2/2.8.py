


s= input("Enter the string")
sub= input("Enter the substring ")
sub2= input("Enter the new substring ")

if sub in s:
    s = s.replace(sub,sub2)
    print(s)