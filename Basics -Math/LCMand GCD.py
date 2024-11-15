class Solution:
    def lcm_and_gcd(self,a,b):
        def gcd(a,b):
            if a==0:
                return b
            elif b==0:
                return a
            else:
                return gcd(a,a%b)
        gcd_val=gcd(a,b)
        lcm=abs(a*b)//gcd_val
        return [lcm,gcd_val]

obj=Solution()
print(obj.lcm_and_gcd(5,10))
print(obj.lcm_and_gcd(7,35))
print(obj.lcm_and_gcd(20,40))
