

n = int(input("Enter the number of names: "))

names = []
for i in range(n):
    name = input(f"Enter name {i+1}: ")
    names.append(name)

names.sort()

print("\nNames in alphabetical order:")
for name in names:
    print(name)
    