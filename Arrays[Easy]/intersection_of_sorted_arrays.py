class Solution:
    def intersection(self,arr1,arr2):
        n1=len(arr1)
        n2=len(arr2)
        i,j=0,0
        intersection=[]
        while i<n1 and j<n2:
            if arr1[i]==arr2[j]:
                if len(intersection)==0 or intersection[-1]!=arr1[i]:
                    intersection.append(arr1[i])
                i+=1
                j+=1
            elif arr1[i]<arr2[j]:
                i+=1
            else:
                j+=1
        return intersection

obj=Solution()
compute=obj.intersection([1,2,3,4,5,],[1,2,3])
print("Intersection of 2 arrays is : ",compute)
