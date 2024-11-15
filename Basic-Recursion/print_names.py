class Solution:
    def print_names(self,n,i=0):
        if i>n:
            return 0
        print("Abi Ayshwariya S")
        self.print_names(n,i+1)


obj=Solution()
obj.print_names(5)
