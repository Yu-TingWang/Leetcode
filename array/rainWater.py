'''
https://leetcode.com/problems/trapping-rain-water/
Leetcode no.42 Trapping Rain Water
'''

'''
Main idea:
the volume of water trapped at height [i] , denote it as v(i)
the base bar at index i , denote it as h(i)
the highest bar before height [i] (inclusive) , max(h[:(i+1)]), denote it as l_max
the highest bar after height [i] (inclusive), max(h[i:]), denote it as r_max
water at h(i) can be trapped between l_max and r_max, 
and if the water goes over the smaller of l_max and r_max, it is going to overflow.
Now, let  g(i) = min(l_max[i],r_max[i])
Hence v(i) = h(i) - g(i)
'''
def trap(height:list)->int:
    '''
    the primitive way. this is going to take O(n^2) time
    '''
    total = 0
    # since there is nothing before h[0], it does not have a l_max
    for i in range(1,len(height)):# O(n)
        l_max = max(height[:(i+1)]) # O(n) <- can be improved
        r_max = max(height[i:])     # O(n) <- can be improved
        total += min(l_max,r_max) - height[i]
    return total

'''
Let's denote g(i) = min(max(h[:(i+1)]),max(h[i:]))
Traverse height to compute g(i) first, and then traverse height again with g(i) to compute v(i)
-------------------------------------------
    bar = [];n = len(height)
    for i in range(1,n):
        for j in range(1,i):
            l_max = max(l_max,height[j])
        for j in range(i,n):
            r_max = max(r_max,height[j])
        bar.append(min(l_max,r_max))
------------------------------------------- This is still taking O(n^2) time
What if we precompute l_max and r_max in O(n) time?
h =     |       a       |    b     |    c      |    d        |
l_max = |       a       | max(a,b) | max(a,b,c)| max(a,b,c,d)|
r_max = | max(d,c,b,a)  |max(d,c,b)|  max(d,c) | max(d)      |
If we translate this pattern to pseudo code, it will be
l_max[1] = h[1]; l_max[i] = max(l_max[i-1],h[i])
r_max[n] = h[n]; r_max[i] = max(h[i],r_max[i+1])
'''
def quicker_trap(height:list)->int:
    '''
    We traverse height for three times. O(n)*3 = O(n)
    And we populate 3 list with space = n . O(n)*3 = O(n)
    Time complexity: O(n)
    Space complexity: O(n)
    >>>quicker_trap([0,1,0,2,1,0,1,3,2,1,2,1])
    6
    left_max == [0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]
    right_max== [3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1]
    >>>quicker_trap([4,2,0,3,2,5])
    9
    left_max == [4, 4, 4, 4, 4, 5]
    right_max== [5, 5, 5, 5, 5, 5]
    '''
    n = len(height)
    left_max = [height[0]]+[0]*(n-1)
    right_max = [0]*(n-1)+[height[-1]]
    for i in range(1,n):
        left_max[i] = max(left_max[i-1],height[i])
    for i in range(n-2,-1,-1):
        right_max[i] = max(height[i],right_max[i+1])
    bar = [0]*n
    for i in range(n):
        bar[i] = min(left_max[i],right_max[i])
    print(left_max,right_max,bar)
    total = 0
    for i in range(n):
        total += bar[i]-height[i]
    return total
'''
height = [1,2,2,3,3,1,4,2,0,0]
--------------------------------
l_max  = [1,2,2,3,3,3,4,4,4,4]
r_max  = [4,4,4,4,4,4,4,2,0,0]
bar    = [1,2,2,3,3,3,4,2,0,0]
From quicker_trap, we notice that:
left_max is always non-decreasing, it either increases or stay the same
right_max is always non-increasing, it either decreases or stay the same
We can take use of their properties of monotonicity.
Since b is the minimum of r_max and l_max at every index i, 
essentially we need to calculate the lower envelope of left_max and right_max for all i.
Each lower envelope, is a lower envelope of one non-increasing function, and one non-decreasing function.
--> two pointers or binary search
height = [1,2,2,3,3,1,4,2,0,0]
          |                 |
          V                 V
          i                 j
we know that l is non-decreasing, so l[j] will be at least 1, and with r[j] = 0, we know that bar[j] must be 0.
'''
def lower_envelop_trap(height:list)->int:
    '''
    Credit:
    https://www.youtube.com/watch?v=XqTBrQYYUcc
    Time complexity:O(n)
    Space complexity: O(1)
    '''
    i = 0
    j = len(height)-1
    if len(height)==0: return 0
    l_max= height[i]
    r_max = height[j]
    total = 0
    while i<=j:
        # move the pointer whose value held is smaller
        # if the values are equal, then it doesn't matter which pointer to move
        l_max = max(l_max,height[i])
        r_max = max(r_max,height[j])
        # take the min of max to be bar
        if l_max < r_max:
            total += l_max - height[i]
            i+=1
        else:#if r_max < l_max:
            total += r_max - height[j]
            j-=1
    return total



if __name__=='__main__':
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(quicker_trap(height))
    h = [4,2,0,3,2,5]
    print(quicker_trap(h))


