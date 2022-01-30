with open("prgm-1.txt") as f:
    content = f.readlines()
content=[x.strip() for x in content]
print(content)
