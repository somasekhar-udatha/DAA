def min_max(arr,n,i,j):
    if(i==j):
        return(arr[i],arr[i])
    if(j-i == 1):
        if(arr[i]<arr[j]):
            return(arr[i],arr[j])
        else:
            return(arr[j],arr[i])
    else:
        mid = (i+j)//2
        lmin,lmax = min_max(arr,n,i,mid)
        rmin,rmax = min_max(arr,n,mid+1,j)
        if(lmin<rmin):
            mini = lmin 
        else:
            mini = rmin 
        if(lmax>rmax):
            maxi = lmax 
        else:
            maxi = rmax
        if(lmin == rmin):
            mini = lmin 
        if(lmax == rmax) :
            maxi = lmax 
        return(mini,maxi)
n = int(input())
arr = list(map(int,input().split()))
i = 0
j = n-1
mini,maxi = min_max(arr,n,i,j)
print(mini,maxi)