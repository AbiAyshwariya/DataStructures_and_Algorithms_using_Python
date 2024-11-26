s=input("Enter the string: ")
hashh={}
for char in s:
    if char in hashh:
        hashh[char]+=1
    else:
        hashh[char]=1
print("Character count: ",hashh)


