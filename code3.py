i=0
for i in range(73):
    name = input("Enter Name : ")
    content = True
    i = 1

    with open("data1.txt") as f:
        while content:
            content = f.readline()
            if name in content.capitalize() :
                print(f"Name is present in line {i}")
                print(content)
            elif name in content.lower() :
                print(f"Name is present in line {i}")
                print(content)
            elif name in content.casefold() :
                print(f"Name is present in line {i}")
                print(content)
            i+=1
    i+=1