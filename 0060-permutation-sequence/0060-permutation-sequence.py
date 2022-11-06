class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i+1) for i in range(n)]
        factorial = math.factorial(n)
        index = k-1
        output = []
        
        while (nums):
            factorial = factorial//len(nums)
            pos = index//factorial
            ans = nums.pop(pos)
            output.append(ans)
            index = index%factorial
            
        return "".join(output)    
        
        
       

            