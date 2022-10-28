#User function Template for python3

def rotate( arr, n):
    i = n-2
    last = arr[-1]
    while i>=0:
        
        arr[i+1]=arr[i]
        i-=1
    arr[0]=last    
    return arr    
    
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        rotate(a, n)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends