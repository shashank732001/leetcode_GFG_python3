#User function Template for python3

class Solution:
    def MedianOfArrays(self, array1, array2):
            #code here
        # lst = sorted(array1+array2)
        # n= len(lst)
        
        # if n%2==0:
        #     a = n//2
        #     if (lst[a-1]%2==0 and lst[a]%2==0) or  (lst[a-1]%2!=0 and lst[a]%2!=0):
        #         return int((lst[a-1]+lst[a])/2)
        #     else:
        #         return ((lst[a-1]+lst[a])/2)
                
            
        # else:
        #     a = n//2
        #     return lst[a]
        
        A, B = array1,array2
        total = len(A) + len(B)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2  # A
            j = half - i - 2  # B

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return int(min(Aright, Bright))
                # even
                elif (max(Aleft, Bleft)%2 and min(Aright, Bright)%2) or (max(Aleft, Bleft)%2==0 and min(Aright, Bright)%2==0):
                    return int((max(Aleft, Bleft) + min(Aright, Bright)) / 2)
                else:
                    return ((max(Aleft, Bleft) + min(Aright, Bright)) / 2)
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
            


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tcs=int(input())

    for _ in range(tcs):
        m = input()
        arr1=[int(x) for x in input().split()]
        n = input()
        arr2=[int(x) for x in input().split()]
        
        
        ob = Solution()
        print(ob.MedianOfArrays(arr1,arr2))

# } Driver Code Ends