n=int(input("Enter the number of elements: "))
arr=[0]*n
hashh={}
for i in range(n):
    arr[i]=int(input(f"Enter the array elements{i+1}: "))
for i in range(n):
    if arr[i] in hashh:
        hashh[arr[i]] += 1
    else:
        hashh[arr[i]] = 1
number=int(input("Enter the number: "))
print(hashh[number])