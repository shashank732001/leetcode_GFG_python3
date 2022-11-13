#User function Template for python3
import heapq
class Solution():
    def mergeHeaps(self, a, b, n, m):
        #your code here
        
        # heap = []
       
        # for ele in a :
            
        #     heap.append(ele)
        # for ele in b:
            
        #     heap.append(ele)
        # # print(heap)
        # heap.sort()
        # heap.reverse()
    
        # return heap    
        
        def MaxHeapify(arr, N, idx):
     
        # Find largest of node and
        # its children
            if idx >= N:
                return
            l = 2 * idx + 1
            r = 2 * idx + 2
            Max = 0
            if l < N and arr[l] > arr[idx]:
                Max = l
            else:
                Max = idx
            if r < N and arr[r] > arr[Max]:
                Max = r
         
            # Put Maximum value at root and
            # recur for the child with the
            # Maximum value
            if Max != idx:
                arr[Max], arr[idx] = arr[idx], arr[Max]
                MaxHeapify(arr, N, Max)
     
            # Builds a Max heap of given arr[0..n-1]
     
         
        def buildMaxHeap(arr, N):
         
            # building the heap from first non-leaf
            # node by calling Max heapify function
            for i in range(int(N / 2) - 1, -1, -1):
                MaxHeapify(arr, N, i)
         
             # Merges Max heaps a[] and b[] into merged[]
        
        
        merged = a+b
        buildMaxHeap(merged, n+m)
        return merged
            



#{ 
 # Driver Code Starts
#Initial Template for Python 3

def isMerged(arr1, arr2, merged):
    if (len(arr1) + len(arr2) != len(merged)):
        return False
    arr1 += arr2
    arr1.sort()
    mergedCopy = sorted(merged)
    if (arr1 != mergedCopy):
        return False
    for i in range(1, len(merged)):
        if merged[i] > merged[(i-1)//2]:
            return False

    return True

if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int, input().split())
        a = [int(i) for i in input().split()]
        b = [int(i) for i in input().split()]
        copyA = a[:]
        copyB = b[:]
        obj = Solution()
        merged = obj.mergeHeaps(a, b, n, m)
        flag = isMerged(copyA, copyB, merged)
        print(0 if flag == False else 1)

# } Driver Code Ends