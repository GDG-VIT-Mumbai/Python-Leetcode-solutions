def binarySearch(nums, target):
    r = 0 #right pointer or index
    l = len(nums)-1 #left pointer or index which is last index of array
    
    while r <= l: #jabtak tumhara right and left index overlap nahi karta tabtak
        mid = r+(l-r)/2 #calculate mid index to find target
        if nums[mid] == target: 
            #if milgaya mid index pe target then return mid index
            return mid
        elif nums[mid] < target:
            r = mid+1
            #nahi mila toh dekho ki mid index wala element agar target se chota hai toh starting searching in left side of array by changing your right pointer
        else:
            l = mid-1
            #else your target might exist in right half of array so shift to right side of array and change left pointer
            
    return -1 #kisi bhi index pe nahi mila toh return -1
    

#time complexity -> O(logn)
#space complexity -> O(1)
