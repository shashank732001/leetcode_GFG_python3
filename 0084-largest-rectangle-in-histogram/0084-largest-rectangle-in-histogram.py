class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        right = []
        left = []
        stackright =[]
        stackleft = []
        res =[]
        arr = heights
        n =len(arr)

        for i in range(n):

            if not stackleft:
                left.append(-1)

            elif stackleft and stackleft[-1][0]<arr[i]:
                left.append(stackleft[-1][1])

            else:
                while stackleft and stackleft[-1][0]>=arr[i]:
                    stackleft.pop()

                if stackleft:
                    left.append(stackleft[-1][1])
                else:
                    left.append(-1)

            stackleft.append([arr[i],i])

        for i in range(n-1,-1,-1):

            if not stackright:
                right.append(n)

            elif stackright and stackright[-1][0]<arr[i]:
                right.append(stackright[-1][1])

            else:
                while stackright and stackright[-1][0]>=arr[i]:
                    stackright.pop()

                if stackright:
                    right.append(stackright[-1][1])
                else:
                    right.append(n)

            stackright.append([arr[i],i])

        # right = right[::-1]	
        maxArea =-10e9
        for i in range(n):
            res.append((right[n-1-i]-left[i]-1)*arr[i])	
            if maxArea<res[i]:
                maxArea =res[i]

        return maxArea
       