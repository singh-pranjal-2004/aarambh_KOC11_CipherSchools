i=0
for i in range(74):
    name = input("\nEnter the Name You Want to Search from Data --> ")
    content = True
    i = 1

    with open("data.txt") as f:
        while content:
            content = f.readline()
            if name in content.capitalize() :
                print(content, end="")
                print(f"Roll number is : {i}",end="\n\n")
            elif name in content.lower() :
                print(content, end="")
                print(f"Roll number is : {i}",end="\n\n")
            elif name in content.casefold() :
                print(content, end="")
                print(f"Roll number is : {i}",end="\n\n")
            i+=1
    i+=1